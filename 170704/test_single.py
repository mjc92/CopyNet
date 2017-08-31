import numpy as np
import torch
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
from models.functions import numpy_to_var, to_np, to_var, visualize, decoder_initial
import time
import sys
import math
torch.manual_seed(1000)

# get vocabulary
w2i = np.load('word2idx.npy').item()
i2w = np.load('idx2word.npy').item()
vocab = Vocab(len(w2i))
vocab.w2i = w2i
vocab.i2w = i2w

# load model
version = 'var_source_code2'
encoder = torch.load(f='models/encoder_%s_%s.pckl' % (version,str(epoch+continue_from)))
decoder = torch.load(f='models/decoder_%s_%s.pckl' % (version,str(epoch+continue_from)))

samples_read = 0
################################# testing ##################################

# 1. for each epoch
# 1.3. initialize entire batch data (no need...
batch.init_batch()

#. 1.4, for each minibatch
test2 = ['var assert = require ( " assert " ) ; var util:==:require (  " util "  ) ;']

correct = 0
total = len(test2)
print_list = []

# 1.4.1. initialize gradient buffers
batch.init_minibatch()

# 1.4.2. obtain batch outputs
data = test2[samples_read:min(samples_read+batch_size,len(test))]
inputs, outputs = batch.process_minibatch(data,vocab)
samples_read+=len(data)

# 1.4.3. inputs and outputs must be unk-ed to put into model w/ limited vocab
unked_inputs = batch.unk_minibatch(inputs,vocab)
unked_outputs = batch.unk_minibatch(outputs,vocab)
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
#             out[2,0,vocab.w2i['codeMirror']]=1
    # remaining states - add results to [out]
    else:
        tmp_out, s, w = decoder(input_idx=unked_decoder_in.squeeze(), encoded=encoded,
                        encoded_idx=inputs, prev_state=s,
                        weighted=w, order=j)
        out = torch.cat([out,tmp_out],dim=1)
    # for debugging: stop if nan
    if math.isnan(w[-1][0][0].data[0]):
        print("NaN detected!")
        sys.exit()

    # 1.8.1. select next input
#         decoder_in = y[:,j] # train with ground truth
    if j==0:
        out[0,-1,vocab.w2i['(']]=1
    decoder_in = out[:,-1,:].max(1)[1] # train with prev outputs
    unked_decoder_in = batch.unk_minibatch(decoder_in.cpu().data.numpy(),vocab)
    unked_decoder_in = Variable(torch.LongTensor(unked_decoder_in).cuda())
# 1.9.1. our targeted outputs should include OOV indices
target_outputs = numpy_to_var(outputs[:,1:])

# 1.9.2. get padded versions of target and output
target = pack_padded_sequence(target_outputs,batch.output_lens.tolist(), batch_first=True)[0]
pad_out = pack_padded_sequence(out,batch.output_lens.tolist(), batch_first=True)[0]
for idx in range(len(data)):
    input_print = []
    truth_print = []
    predict_print = []
    for i in inputs[idx]:
        if i==0:
            break
        else:
            input_print.append(i)
    for i in outputs[idx]:
        if i==3:
            break
        elif i==2:
            pass
        else:
            truth_print.append(i)
    for i in out[idx,:,:].max(1)[1].cpu().data.numpy():
        if i==3:
            break
        else:
            predict_print.append(i)
    line0 = "\n==================================================================="
    line1 = 'Input1:       '+''.join(vocab.idx_list_to_word_list(input_print, batch.idx2oov_list[idx]))
    line2 = 'Output:       '+''.join(vocab.idx_list_to_word_list(truth_print, batch.idx2oov_list[idx]))
    line3 = 'Predict[UNK]: '+''.join(vocab.idx_list_to_word_list(predict_print))
    line4 = 'Predicted:    '+''.join(vocab.idx_list_to_word_list(predict_print, batch.idx2oov_list[idx]))
    line1 = line1.replace('var', 'var ')
    line1 = line1.replace(';',';\nInput2:       ')
    line2 = line2.replace('var', 'var ')
    line3 = line3.replace('var', 'var ')
    line4 = line4.replace('var', 'var ')
    if line2[14:]==line4[14:]:
        correct+=1
        line4+='\n***CORRECT***'
# with open('test_results_%s_epoch_%d_acc_%1.3f.txt' 
#           %(version,epoch+continue_from,correct*1.0/total),'w') as f:
#     f.write('\n'.join(print_list))