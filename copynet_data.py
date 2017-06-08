# import numpy as np

# vocab = 1000
# # eos : 0
# # padding : 1

# # we stick to rule 1 : 2 3 4 5 100 6 7 -> 4 5 100 8
# # there will be 200 different instances for 200 different rules

# total_list = []
# for i in range(200):
# 	# set sequence
# 	values = np.random.randint(3,vocab,20) # creates 20 random numbers
# 	values = list(values)
# 	in_ = np.random.randint(3,15) # length of input
# 	out_ = np.random.randint(3,20-in_) # length of output
# 	in_insert = np.random.randint(0,in_) # where to insert string
# 	out_insert = np.random.randint(0,out_) # where to insert string
# 	in_list = values[:in_]
# 	out_list = values[in_:in_+out_]
# 	for j in range(200):
# 		x_len = np.random.randint(1,15)
# 		x = np.random.randint(2,vocab, x_len)
# 		x = list(x)
# 		# x is the string to be copied
# 		in_str = in_list[:in_insert]+x+in_list[in_insert:]
# 		out_str = out_list[:out_insert]+x+out_list[out_insert:]
# 		in_str = [str(i) for i in in_str]
# 		out_str = [str(i) for i in out_str]
# 		x_str = [str(i) for i in x]
# 		in_str = ','.join(in_str)
# 		out_str = ','.join(out_str)
# 		x_str = ','.join(x_str)
# 		total_list.append(in_str+'\t'+out_str+'\t'+x_str)
# total_list = '\n'.join(total_list)
# with open('data/copynet_data.txt','w') as f:
# 	f.write(total_list)

import numpy as np

vocab = 10
# eos : 0
# padding : 1

# we stick to rule 1 : 2 3 4 5 100 6 7 -> 4 5 100 8
# there will be 200 different instances for 200 different rules

total_list = []
out_str = [1,2,3,4,5,6,7,8,9]
out_str = [str(x) for x in out_str]
out_str = ','.join(out_str)
for i in range(200):
	# set sequence
	values = np.random.randint(3,vocab,5) # creates 20 random numbers
	values = list(values)
	in_ = np.random.randint(3,10) # length of input
	out_ = np.random.randint(3,100-in_) # length of output
	in_insert = np.random.randint(0,in_) # where to insert string
	out_insert = np.random.randint(0,out_) # where to insert string
	in_list = values[:in_]
	out_list = values[in_:in_+out_]
	for j in range(200):
		x_len = np.random.randint(1,5)
		x = np.random.randint(2,vocab, x_len)
		x = list(x)
		# x is the string to be copied
		in_str = in_list[:in_insert]+x+in_list[in_insert:]
		# out_str = out_list[:out_insert]+x+out_list[out_insert:]
		in_str = [str(i) for i in in_str]
		# out_str = [str(i) for i in out_str]
		x_str = [str(i) for i in x]
		in_str = ','.join(in_str)
		# out_str = ','.join(out_str)
		x_str = ','.join(x_str)
		total_list.append(in_str+'\t'+out_str+'\t'+x_str)
total_list = '\n'.join(total_list)
with open('data/copynet_data_simple.txt','w') as f:
	f.write(total_list)