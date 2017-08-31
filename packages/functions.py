import numpy as np
import spacy
import torch
from torch.autograd import Variable
import os
from collections import Counter
import torch
import glob
from spacy import attrs

def parse_cnn(file_dir, nlp):
	with open(file_dir) as f:
		text = f.read()
		text = text.lower()
		text = text.replace('\n\n',' ')
		text = text.split("@highlight")
		body = nlp(text[0])
		body_words = [x.text for x in list(body)]
		summaries = text[1:]
		summaries = ' '.join([x+'.' for x in summaries])
		summaries = nlp(summaries)
		summary_words = [x.text for x in list(summaries)]
		return body_words, summary_words

def word_list_to_idx_list(word_list, word2idx, vocab_size):
	out = []
	oov2idx = dict()
	oov_words = []
	for word in word_list:
		try:
			out.append(word2idx[word])
		except KeyError:
			if word not in oov2idx:
				oov2idx[word]=vocab_size+len(oov2idx)
			out.append(oov2idx[word])
	return out

def calc_running_avg_loss(loss, running_avg_loss, step, decay=0.99):
	if running_avg_loss==0:
		running_avg_loss = loss
	else:
		running_avg_loss = running_avg_loss * decay + (1-decay) * loss
	running_avg_loss = min(running_avg_loss,12) # clip
	return running_avg_loss

def to_cuda(item):
	if torch.cuda.is_available():
		return item.cuda()
	else:
		return item

def num_to_var(item):
	# numpy array to Variable
	if item.dtype==int:
		out = Variable(torch.LongTensor(item))
	else:
		out = Variable(torch.Tensor(item))
	return to_cuda(out)
		