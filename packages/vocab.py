from collections import Counter
import pickle
import spacy

class Vocab(object):

	def __init__(self, max_size):
		self.w2i = {}
		self.i2w = {}
		self.count = 0
		self.max_size = max_size
		self.nlp = spacy.load('en')
		self.counter = Counter()

		for w in ['<PAD>','<UNK>','<SOS>','<EOS>']:
			self.w2i[w] = self.count
			self.i2w[self.count] = w
			self.count +=1

	# def add_from_counter_list(self, counter_list):
	# 	# list takes form of [(word, freq), (word, freq), ..., ]

	def word2idx(self, word):
		if word not in self.w2i:
			return self.w2i['<UNK>']
		return self.w2i[word]

	def idx2word(self, idx):
		if idx not in self.i2w:
			return '<UNK>'
		return self.i2w[idx]

	# changes an indices list to a word list
	# can include idx2oov dictionary to change oov words
	
	def create_oov_list(self, word_list, max_oovs):
		# creates oov2idx and idx2oov from a given sequence
		# max_oovs: maximum number of OOVs allowed
		oov2idx = {}
		idx2oov = {}
		oov_count=0
		for word in word_list:
			if (word not in oov2idx) & (word not in self.w2i):
				oov2idx[word] = self.count + oov_count
				idx2oov[self.count+oov_count] = word
				oov_count+=1
			if oov_count>=max_oovs:
				return oov2idx, idx2oov
		return oov2idx,idx2oov

	def idx_list_to_word_list(self, idx_list, idx2oov={}):
		# idx2oov: contains {oov_idx: oov_word,  such as 50000:Thompson}
		if type(idx_list[0])!=int:
			idx_list = [int(idx) for idx in idx_list]
		out = []
		for idx in idx_list:
			if idx in idx2oov:
				out.append(idx2oov[idx])
			else:
				out.append(self.idx2word(idx))
		return out

	# changes a word list to an indices list
	# can preserve oov words by creating a temporary dictionary and index

	def word_list_to_idx_list(self, word_list, oov2idx={}):
		# oov2idx: temporary dictionary of the oov words introduced per sample
		out = []
		for word in word_list:
			if word in oov2idx:
				out.append(oov2idx[word])
			else:
				out.append(self.word2idx(word))
		return out

	def add_to_vocab(self, word_list):
		# add a list of words to the vocabulary if the words do not exist
		for word in word_list:
			if self.count>=self.max_size:
				print("Vocabulary max size reached!")
				return
			else:
				if (word not in self.w2i) & (word not in ['<PAD>','<S>','</S>','<UNK>']):
					self.w2i[word]=self.count
					self.i2w[self.count]=word
					self.count+=1

	def tokenize(self, text):
		# using spacy, tokenizes a sentence or sentences into a list of words (strings)
		tokenized = self.nlp(text)
		out = [x.text for x in tokenized]
		return out

	def feed_to_counter(self, word_list):
		# when given a word list, add it to the counter in this Vocab object
		counter = Counter(word_list)
		self.counter = self.counter + counter
		return

	def preprocess_string(self, text, preprocess_list):
		# when given a list of tuples (e.g. ("  ", " ")), preprocesses string
		for tup in preprocess_list:
			from_str, to_str = tup
			text = text.replace(from_str, to_str)
		return text

	def counter_to_vocab(self, counter):
		# fills in the vocabulary from a Counter object
		word_list = [tup[0] for tup in counter.most_common()[:self.max_size]]
		self.add_to_vocab(word_list)
