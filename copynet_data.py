import numpy as np

# vocab, num_cases, sample_per_case, ab_max, x_max, ver = [100,1,1000,5,5,'v1']
# vocab, num_cases, sample_per_case, ab_max, x_max, ver = [100,10,1000,5,5,'v2']
# vocab, num_cases, sample_per_case, ab_max, x_max, ver = [100,10,1000,5,15,'v3']
# vocab, num_cases, sample_per_case, ab_max, x_max, ver = [100,3,1000,5,15,'v4']
# vocab, num_cases, sample_per_case, ab_max, x_max, ver = [100,200,200,5,5,'v5']
vocab, num_cases, sample_per_case, ab_max, x_max, ver = [1000,1,1000,5,5,'v6']
# padding : 0
# eos : 1
# sos : 2

total_list = []
for i in range(num_cases):
	# set sequence
	in1_ = np.random.randint(1,ab_max) # length of input
	in2_ = np.random.randint(1,ab_max) # length of input
	out1_ = np.random.randint(1,ab_max) # length of output
	out2_ = np.random.randint(1,ab_max) # length of output
	in1 = list(np.random.randint(3,vocab,in1_))
	in2 = list(np.random.randint(3,vocab,in2_))
	out1 = list(np.random.randint(3,vocab,out1_))
	out2 = list(np.random.randint(3,vocab,out2_))
	for j in range(sample_per_case):
		val_ = np.random.randint(1,x_max) # length of X
		values = np.random.randint(3,vocab,val_) # creates N random numbers
		values = list(values)
		in_list = in1 + values + in2
		out_list = out1 + values + out2
		in_list = [str(i) for i in in_list]
		out_list = [str(i) for i in out_list]
		values = [str(i) for i in values]
		in_str = ','.join(in_list)
		out_str = ','.join(out_list)
		x_str = ','.join(values)
		total_list.append(in_str+'\t'+out_str+'\t'+x_str)
total_list = '\n'.join(total_list)
with open('data/copynet_data_'+ver+'.txt','w') as f:
	f.write(total_list)
