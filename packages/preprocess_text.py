# changes all words to indices
# also adds vocab+N indices for OOV words

import numpy as np
import spacy
import os
from collections import Counter
import torch
import glob
from spacy import attrs


word2idx = np.load('word2idx.npy').item()
vocab_size = len(word2idx)
batch_size = 100

nlp = spacy.load('en') # loads default English object
cnn_dir = '/home/mjc/datasets/CNN_DailyMail/cnn/stories/'
cnn_pre_dir = '/home/mjc/datasets/CNN_DailyMail/cnn/preprocessed_stories/'

file_list = [os.path.join(cnn_dir,file) for file in os.listdir(cnn_dir)]
total_files = len(file_list)
files_read = 0
count = 0
for file in file_list:
	with open(file) as f:
		text = f.read()
		text = text.lower()
		text = text.replace('\n\n',' ')
		text = text.replace('(cnn)','')
		text = text.split("@highlight")
		body = text[0]
		body_words = body.split(' ')
		summaries = ' . '.join(text[1:])+' .'
		summary_words = summaries.split(' ')
		unique_words = list(set(body_words+summary_words))
		temp_dict = dict()
		oovs = 0
		for w in unique_words:
			try:
				temp_dict[w] = word2idx[w]
			except KeyError:
				oovs+=1
				temp_dict[w] = oovs+vocab_size
		body_idx = [str(temp_dict[x]) for x in body_words]
		summary_idx = [str(temp_dict[x]) for x in summary_words]
		out = ' '.join(body_idx)+'::'+' '.join(summary_idx)
		out_file = file.replace('/stories/','/preprocessed_stories/')
	with open(out_file,'w') as f:
		f.write(out)
	count+=1
	if count%100==0:
		print(count)


# 		doc = nlp(text)


# counter = Counter()
# while (files_read<total_files):
#     word_list = []
#     batch_files = file_list[files_read:min(files_read+1000,total_files)]
#     for file_name in batch_files:
#         with open(file_name) as f:
#             text = f.read()
#             text = text.lower()
#             text = text.replace('\n\n',' ')
#             text = text.replace('(cnn)','')
#             text = text.split("@highlight")
#             body = text[0]
#             doc = list(nlp(body))
#             word_list.extend([x.text for x in doc])

#     counter = counter + Counter(word_list)
#     files_read+=len(batch_files)
#     print("%d files read so far..." % files_read)
#     word2idx = {tup[0]: i for i,tup in enumerate(counter.most_common(vocab_size))}
#     np.save('word2idx.npy',word2idx)
# print("All merged!")
# word2idx = {tup[0]: i for i,tup in enumerate(counter.most_common(vocab_size))}
# np.save('word2idx.npy',word2idx)