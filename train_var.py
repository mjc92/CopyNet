import numpy as np
import torch
import random
import pickle
import os
from packages.vocab import Vocab
from packages.batch import Batch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from torch.autograd import Variable
import torch.nn.functional as F
from models.copynet_dbg import CopyEncoder, CopyDecoder
from models.functions import numpy_to_var, to_np, to_var, visualize, decoder_initial, update_logger
import time
import sys
import math
torch.manual_seed(1000)

# Hyperparameters
embed_size = 150
hidden_size = 300
num_layers = 1
bin_size = 10
num_epochs = 10
prev_end=0
max_oovs = 12
batch_size = 100
lr = 0.001
vocab_size = 1000
weight_decay = 0.99
use_saved = False # whether to train from a previous model
continue_from = 0
step = 0 # number of steps taken
teacher_force = True
version = 'var_source_code3'

# get vocabulary
print("Loading vocab...")
vocab = Vocab(vocab_size)
vocab.w2i = np.load('js_dataset/w2i.npy').item()
vocab.i2w = np.load('js_dataset/i2w.npy').item()
vocab.count = len(vocab.w2i)
print("Vocabulary loaded!")

# get training and test data
file_dir = 'data/data.txt'
# train_dir = 'data/js_dataset/var_dataset_5_train.txt'
# test_dir = 'data/js_dataset/var_dataset_5_test.txt'
print("Opening files...")

with open(file_dir) as f:
    lines = f.readlines()
    # lines = [line.strip() for line in train]


# with open(train_dir) as f:
#     train = f.readlines()
#     train = [line.strip() for line in train]

# with open(test_dir) as f:
#     test = f.readlines()
#     test = [line.strip() for line in test]

lines = [line.strip() for line in lines]
lines = list(set(lines))
test_size = int(len(lines)*0.3)
import random
random.shuffle(lines)
test = lines[:test_size]
train = lines[test_size:]
with open('data/var_dataset_train.txt','w') as f:
    f.write('\n'.join(train))
with open('data/var_dataset_test.txt','w') as f:
    f.write('\n'.join(test))
print("Files opened!")
# random.shuffle(train)

print("Creating batch object...")
batch = Batch(file_list=[],max_in_len=30,max_out_len=30, max_oovs=max_oovs)
batch.num_of_minibatch=len(train)/batch_size

# get number of batches
num_samples = len(train)
num_batches = int(num_samples/batch_size)

encoder = CopyEncoder(vocab_size, embed_size, hidden_size)
decoder = CopyDecoder(vocab_size, embed_size, hidden_size)
continue_from = 0
if torch.cuda.is_available():
    encoder.cuda()
    decoder.cuda()

################################# training ##################################

# set loss
criterion = nn.NLLLoss()
start = time.time()

# 1. for each epoch
for epoch in range(num_epochs):
    print("==================================================")
    print("Epoch ",epoch+1)

    # 1.1. reset optimizers
    opt_e = optim.Adam(params=encoder.parameters(), lr=lr)
    opt_d = optim.Adam(params=decoder.parameters(), lr=lr)
    lr= lr * weight_decay # weight decay

    # 1.2. shuffle data
    random.shuffle(train)
    samples_read = 0

    # 1.3. initialize entire batch data (no need...
    batch.init_batch()

    #. 1.4, for each minibatch
    while(samples_read<len(train)):

        # 1.4.1. initialize gradient buffers
        opt_e.zero_grad()
        opt_d.zero_grad()
        batch.init_minibatch()

        # 1.4.2. obtain batch outputs
        data = train[samples_read:min(samples_read+batch_size,len(train))]
        inputs, outputs = batch.process_minibatch(data,vocab)
        samples_read+=len(data)

        # 1.4.3. inputs and outputs must be unk-ed to put into model w/ limited vocab
        unked_inputs = batch.unk_minibatch(inputs,vocab)
        unked_outputs = batch.unk_minibatch(outputs,vocab)

        # initially all is learned through given answers (False)
        # the ratio for teacher forcing increases gradually
        if np.random.random_sample(size=1)[0]<(epoch*1.0/num_epochs):
            teacher_force = True
        else:
            teacher_force = False


        x = numpy_to_var(unked_inputs)
        y = numpy_to_var(unked_outputs)

        # 1.5. encoded outputs
        encoded, _ = encoder(x)

        # 1.6.1. get initial input of decoder
        decoder_in, s, w = decoder_initial(x.size(0))
        decoder_in = y[:,0]

        # 1.7. for each decoder timestep
        for j in range(y.size(1)-1): # for all sequences
            """
            decoder_in (Variable): [b]
            encoded (Variable): [b x seq x hid]
            input_out (np.array): [b x seq]
            s (Variable): [b x hid]
            """
            # 1.7.1.1st state - create [out]
            if j==0:
                out, s, w = decoder(input_idx=y[:,j], encoded=encoded,
                                encoded_idx=inputs, prev_state=s,
                                weighted=w, order=j)
            # remaining states - add results to [out]
            else:
                tmp_out, s, w = decoder(input_idx=y[:,j], encoded=encoded,
                                encoded_idx=inputs, prev_state=s,
                                weighted=w, order=j)
                out = torch.cat([out,tmp_out],dim=1)
            # for debugging: stop if nan
            if math.isnan(w[-1][0][0].data[0]):
                print("NaN detected!")
                sys.exit()

            # 1.8.1. select next input
            if teacher_force:
                decoder_in = out[:,-1,:].max(1)[1].cpu().data.numpy().squeeze()
            else:
                decoder_in = y[:,j] # train with ground truth


        # 1.9.1. our targeted outputs should include OOV indices
        target_outputs = numpy_to_var(outputs[:,1:])

        # 1.9.2. get padded versions of target and output
        target = pack_padded_sequence(target_outputs,batch.output_lens.tolist(), batch_first=True)[0]
        pad_out = pack_padded_sequence(out,batch.output_lens.tolist(), batch_first=True)[0]

        # include log computation as we are using log-softmax and NLL
        pad_out = torch.log(pad_out)
        loss = criterion(pad_out, target)
        loss.backward()

        elapsed = time.time()
        print("Elapsed time for single batch: %1.3f" %(elapsed-start))
        start = time.time()

        if samples_read%100==0:
            print("[%d/%d] Loss: %1.4f"%(samples_read,len(train),loss.data[0]))
        opt_e.step()
        opt_d.step()
        step += 1
        info = {
            'loss': loss.data[0]
        }
        del loss
        del out
        del pad_out
        del tmp_out
        # save model temporarily
        if samples_read%10000==0:
            torch.save(f='models/encoder_%s_temp.pckl' % (version),obj=encoder)
            torch.save(f='models/decoder_%s_temp.pckl' % (version),obj=decoder)
    # print("Loss: ",loss.data[0])
    elapsed = time.time()
    time_per_epoch = elapsed-start
    print("Elapsed time for epoch: %1.3f" %time_per_epoch)
    print("Remaining time: %1.3f" % (time_per_epoch*(num_epochs-epoch)))
    start = time.time()

    torch.save(f='models/encoder_%s_%s.pckl' % (version,str(epoch+continue_from)),obj=encoder)
    torch.save(f='models/decoder_%s_%s.pckl' % (version,str(epoch+continue_from)),obj=decoder)