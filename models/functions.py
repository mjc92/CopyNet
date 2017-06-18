import torch
import matplotlib.pyplot as plt
import numpy as np
from torch.autograd import Variable

# changes a numpy array to a Variable of LongTensor type
def numpy_to_var(x,is_int=True):
    if is_int:
        x = torch.LongTensor(x)
    else:
        x = torch.Tensor(x)
    if torch.cuda.is_available():
        x = x.cuda()
    return Variable(x)

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
        inputs, outputs, _ = line.split('\t')
        inputs_.append([int(num) for num in inputs.split(',')]+[1])
        outputs_.append([int(num) for num in outputs.split(',')]+[1])
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

def to_np(x):
    return x.data.cpu().numpy()

def to_var(x):
    if torch.cuda.is_available():
        x = x.cuda()
    return Variable(x)

def visualize(x):
    plt.pcolor(x.cpu().data.numpy())

def decoder_initial(batch_size):
    decoder_in = torch.LongTensor(np.ones(batch_size,dtype=int))*2
    s = None
    w = None
    if torch.cuda.is_available():
        decoder_in = decoder_in.cuda()
    decoder_in = Variable(decoder_in)
    return decoder_in, s, w

def update_logger(logger,list_of_models,loss, step):
    # logger: ext. function defined by yunjey
    # list_of_models: [encoder, decoder]
    # step : current step
    info = {
        'loss': loss.data[0]
    }
    encoder, decoder = list_of_models
    for tag, value in info.items():
        logger.scalar_summary(tag,value,step)

    for tag, value in encoder.named_parameters():
        tag = 'encoder/'+tag
        logger.histo_summary(tag, to_np(value), step)
        logger.histo_summary(tag+'/grad', to_np(value.grad), step)

    for tag, value in decoder.named_parameters():
        tag = 'decoder/'+tag
        logger.histo_summary(tag, to_np(value), step)
        logger.histo_summary(tag+'/grad', to_np(value.grad), step)
    return logger