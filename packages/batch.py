import os
import numpy as np

class Batch(object):
	def __init__(self, file_list, max_in_len, max_out_len, max_oovs):
		self.num_of_minibatch = len(file_list) # number of minibatches to read
		self.minibatch_count = 0 # how many minibatches read so far
		self.end_of_batch = False # whether we have reached the end of a batch
		self.max_in_len = max_in_len # maximum length of encoder input
		self.max_out_len = max_out_len # maximum length of decoded output
		# per minibatch
		self.minibatch_size = 0 # number of samples in a particula minibatch
		self.oov2idx_list = [] 
		self.idx2oov_list = []
		self.input_lens = [] # lengths of encoding sequences within a batch 
		self.output_lens = [] # lengths of decoding sequences within a batch 
		self.max_oovs = max_oovs # max. number of OOVs possible

	# def get_minibatch(self,batch_list, vocab, deliminator=":==:"):
	# 	"""
	# 	Args.
	# 	batch_list : list of samples
	# 	vocab : a vocab object
	# 	"""

	# 	# releases a minibatch list & splits into stories and summaries
	# 	if self.end_of_batch == True:
	# 		print ("Trying to call from end of batch!")
	# 		return None
	# 	if self.sample_count+self.batch_size<self.len_samples:
	# 		out = batch_list[self.sample_count:self.sample_count+self.batch_size]
	# 		self.sample_count += self.batch_size
	# 	else: # end of batch
	# 		out = batch_list[self.sample_count:self.len_samples]
	# 		self.end_of_batch = True

	# 	# splits this list into story and summary
	# 	stories = []
	# 	summaries = []
	# 	for line in out:
	# 		story, summary = line.split(deliminator)
	# 		stories.append(vocab.tokenize(story))
	# 		summaries.append(vocab.tokenize(summary))

	# 	stories = self.match_minibatch_lengths()

	# 	# fixes lengths
	# 	return stories, summaries

	def process_minibatch(self,minibatch, vocab, deliminator=":==:"):
		"""
		Args.
		minibatch : text corpus or list
		vocab : a vocab object
		"""

		# splits this list into stories and summaries
		stories = []
		summaries = []
		if type(minibatch)==str:
			minibatch = minibatch.split('\n\n')
		self.minibatch_size = len(minibatch)
		# for each sample in minibatch
		for line in minibatch:			
			# split each line into a story and a summary (word lists)
			story, summary = line.split(deliminator)
			story = vocab.tokenize(story)[:self.max_in_len]
			summary = vocab.tokenize(summary)[:self.max_out_len-2]
			summary = ['<SOS>']+summary+['<EOS>']

			# get all oov words from this sample and append them to list
			oov2idx, idx2oov = vocab.create_oov_list(story+summary, self.max_oovs)
			self.oov2idx_list.append(oov2idx)
			self.idx2oov_list.append(idx2oov)
			# now change these into idx lists
			story = vocab.word_list_to_idx_list(story,oov2idx)
			summary = vocab.word_list_to_idx_list(summary,oov2idx)
			# append these to a list so that we have all stories/sums for a minibatch
			stories.append(story)
			summaries.append(summary)
		# returns [b x max_seq] matrices which are indiced with numbers and zero padding
		stories, summaries = self.match_minibatch_lengths(vocab, stories, summaries)
		return stories, summaries

	# initialize batch use at end of every epoch
	def init_batch(self):
		self.batch_count = 0
		self.end_of_batch = False

	# initialize minibatch values at end of every minibatch
	def init_minibatch(self):
		self.oov2idx_list = [] 
		self.idx2oov_list = []
		self.input_lens = [] 
		self.output_lens = []
		self.oov_len = 0

	def match_minibatch_lengths(self, vocab, story_list, summary_list):
		"""
		Args:
		story_list: list of story tokens
		summary_list: list of summary tokens, <SOS> and <EOS> are not added so far
		"""
		# story_list = [x[:self.max_in_len] for x in story_list]
		# summary_list = [ [vocab.w2i['<SOS>']] + x[:self.max_out_len-2] +
		# [vocab.w2i['<EOS>']] for x in summary_list] # add <SOS> and <EOS>
		# get max lengths
		in_len = np.array([len(line) for line in story_list])
		out_len = np.array([len(line) for line in summary_list])

		max_in = max(in_len)
		max_out = max(out_len)
		# create numpy arrays to store indices
		stories_out = np.zeros([self.minibatch_size,max_in],dtype=int)
		summaries_out = np.zeros([self.minibatch_size,max_out],dtype=int)
		for b in range(self.minibatch_size):
			stories_out[b][:in_len[b]] = np.array(story_list[b])
			summaries_out[b][:out_len[b]] = np.array(summary_list[b])
		# get summary lengths in descending order
		out_rev = out_len.argsort()[::-1]
		# return final values
		self.oov2idx_list = [self.oov2idx_list[i] for i in out_rev]
		self.idx2oov_list = [self.idx2oov_list[i] for i in out_rev]
		self.oov_len = max([len(x) for x in self.oov2idx_list])
		self.input_lens = in_len[out_rev]
		self.output_lens = out_len[out_rev]
		return stories_out[out_rev], summaries_out[out_rev]

	def unk_minibatch(self, minibatch, vocab):
		# for a numpy array minibatch, put all unks to zero
		unk_idx = vocab.w2i['<UNK>']
		vocab_idxs = np.array(minibatch<vocab.count,dtype=int)
		oov_idxs = np.array(minibatch>=vocab.count,dtype=int) * unk_idx
		out = np.multiply(vocab_idxs, minibatch) # all OOV words are set to 0
		return out + oov_idxs # OOV words are instead set to UNK

