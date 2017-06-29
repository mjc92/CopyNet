def toData(batch):
    # [input] batch: list of strings
    # [output] input_out, output_out: np array([b x seq]), fixed size, eos & zero padding applied
    # [output] in_idx, out_idx: np.array([b]), length of each line in seq
    batch = [line.replace('\n','') for line in batch]
    inputs_ = []
    outputs_ = []
    in_len = []
    out_len = []
    for line in batch:
        inputs, outputs = line.split('::')
        inputs_.append([int(num) for num in inputs.split(' ')])
        outputs_.append([int(num) for num in outputs.split(' ')])
        in_len.append(len(inputs_[-1]))
        out_len.append(len(outputs_[-1]))
    in_len = np.array(in_len)
    out_len = np.array(out_len)
    max_in = max(in_len)
    max_out = max(out_len)
    batch_size = len(batch)
    input_out = np.zeros([batch_size,max_in],dtype=int)
    output_out = np.zeros([batch_size,max_out],dtype=int)
    for b in range(batch_size):
        input_out[b][:in_len[b]] = np.array(inputs_[b])
        output_out[b][:out_len[b]] = np.array(outputs_[b])
    out_rev = out_len.argsort()[::-1]
    return input_out[out_rev], output_out[out_rev], in_len[out_rev], out_len[out_rev]

import numpy as np
w2i = np.load('data/en-django/en-django/w2i.npy').item()
i2w = np.load('data/en-django/en-django/i2w.npy').item()
vocab_size = len(w2i)
print(vocab_size)

import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from torch.autograd import Variable
import torch.nn.functional as F
from models.copynet import CopyEncoder, CopyDecoder
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
num_epochs = 40
prev_end=0
batch_size = 50
lr = 0.001
vocab_size = 100
weight_decay = 0.99
use_saved = False # whether to train from a previous model
continue_from = 0
version = 'django_fixed'
step = 0 # number of steps taken

# input and output directories
w2i = np.load('data/en-django/en-django/w2i.npy').item()
i2w = np.load('data/en-django/en-django/i2w.npy').item()
vocab_size = len(w2i)
file_dir = 'data/en-django/en-django/idx_lists_fixed.txt'
# get training and test data
with open(file_dir) as f:
    lines = f.readlines()

import random
random.shuffle(lines)
test = lines[:200]
train = lines[200:]

# get number of batches
num_samples = len(train)
num_batches = int(num_samples/batch_size)


################ load copynet model #####################
if use_saved:
    # if using from previous data
    encoder_dir = 'models/encoder_%s_%s.pckl' % (version,continue_from)
    decoder_dir = 'models/decoder_%s_%s.pckl' % (version,continue_from)
    encoder = torch.load(f=encoder_dir)
    decoder = torch.load(f=decoder_dir)
else:
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
for epoch in range(num_epochs):
    print("==================================================")
    print("Epoch ",epoch+1)
    opt_e = optim.Adam(params=encoder.parameters(), lr=lr)
    opt_d = optim.Adam(params=decoder.parameters(), lr=lr)
    lr= lr * weight_decay # weight decay
    # shuffle data
    random.shuffle(train)
    samples_read = 0
    while(samples_read<len(train)):
        # initialize gradient buffers
        opt_e.zero_grad()
        opt_d.zero_grad()

        # obtain batch outputs
        batch = train[samples_read:min(samples_read+batch_size,len(train))]
        input_out, output_out, in_len, out_len = toData(batch)
        input_out = input_out[:,:50]
        in_len = np.array([min(50,x) for x in in_len])
        output_out = output_out[:,:50]
        out_len = np.array([min(50,x) for x in out_len])
#         print(in_len.shape)
#         print(out_len.shape)
        samples_read+=len(batch)

        # mask input to remove padding
        input_mask = np.array(input_out>0, dtype=int)

        # input and output in Variable form
        x = numpy_to_var(input_out)
        y = numpy_to_var(output_out)

        # apply to encoder
        encoded, _ = encoder(x)

        # get initial input of decoder
        decoder_in, s, w = decoder_initial(x.size(0))

        # out_list to store outputs
        out_list=[]
        for j in range(y.size(1)): # for all sequences
            """
            decoder_in (Variable): [b]
            encoded (Variable): [b x seq x hid]
            input_out (np.array): [b x seq]
            s (Variable): [b x hid]
            """
            # 1st state
#             print(j)
#             print(out.size())
            if j==0:
                out, s, w = decoder(input_idx=decoder_in, encoded=encoded,
                                encoded_idx=input_out, prev_state=s,
                                weighted=w, order=j)
            # remaining states
            else:
                tmp_out, s, w = decoder(input_idx=decoder_in, encoded=encoded,
                                encoded_idx=input_out, prev_state=s,
                                weighted=w, order=j)
                out = torch.cat([out,tmp_out],dim=1)
            # for debugging: stop if nan
            if math.isnan(w[-1][0][0].data[0]):
                sys.exit()
            # select next input

 
            decoder_in = y[:,j] # train with ground truth
#             out_list.append(out[:,-1].max(1)[1].squeeze().cpu().data.numpy())

        # print(torch.stack(decoder.prob_c_to_g,1))
        target = pack_padded_sequence(y,out_len.tolist(), batch_first=True)[0]
        pad_out = pack_padded_sequence(out,out_len.tolist(), batch_first=True)[0]
        # include log computation as we are using log-softmax and NLL
        pad_out = torch.log(pad_out)
        loss = criterion(pad_out, target)
        loss.backward()
        if samples_read%100==0:
            print("[%d/%d] Loss: %1.4f"%(samples_read,len(train),loss.data[0]))
        opt_e.step()
        opt_d.step()
        step += 1
        info = {
            'loss': loss.data[0]
        }
    # print("Loss: ",loss.data[0])
    elapsed = time.time()
    print("Elapsed time for epoch: ",elapsed-start)
    start = time.time()

    torch.save(f='models/encoder_%s_%s.pckl' % (version,str(epoch+continue_from)),obj=encoder)
    torch.save(f='models/decoder_%s_%s.pckl' % (version,str(epoch+continue_from)),obj=decoder)
