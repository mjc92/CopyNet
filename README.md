# Incorporating Copying Mechanism in Sequence-to-Sequence Learning

## Abstract

> We address an important problem in sequence-to-sequence (Seq2Seq) learning referred to as copying, in which certain segments in the input sequence are selectively replicated in the output sequence. A similar phenomenon is observable in human language communication. For example, humans tend to repeat entity names or even long phrases in conversation. The challenge with regard to copying in Seq2Seq is that new machinery is needed to decide when to perform the operation. In this paper, we incorporate copying into neural network-based Seq2Seq learning and propose a new model called CopyNet with encoder-decoder structure. CopyNet can nicely integrate the regular way of word generation in the decoder with the new copying mechanism which can choose sub-sequences in the input sequence and put them at proper places in the output sequence. Our empirical study on both synthetic data sets and real world data sets demonstrates the efficacy of CopyNet. For example, CopyNet can outperform regular RNN-based model with remarkable margins on text summarization tasks.

## About

A PyTorch implementation of CopyNet by Minje Choi.

## Observations & Results

Tested on Django
- 19,000 lines of source code <-> annotation pairs

## Task
Generating human-like comments from raw source code lines
- includes identifier/class/function name
- number of arguments for a function method
- describes what the function does

## How To Run

```
python train.py
```

## Examples
```Python
[INPUT]
self . keyOrder . append ( key )
[GROUND TRUTH]
# append key to self . keyOrder .
[PREDICTED]
# append key to self . keyOrder .

[INPUT]
str_number = str_number [ 1 : ]
[GROUND TRUTH]
# remove the first element from str_number .
[PREDICTED]
# substitute first element of str_number for str_number .

[INPUT]
return { }
[GROUND TRUTH]
# return an empty dictionary .
[PREDICTED]
# return an empty dictionary .

[INPUT]
return 12
[GROUND TRUTH]
# return integer 12 .
[PREDICTED]
# return 12 .

[INPUT]
warnings . warn ( " cache_choices has been deprecated and will be " " removed in Django 1 . 9 . " , RemovedInDjango19Warning , stacklevel = 2 )
[GROUND TRUTH]
# call the function warnings . warn with 3 arguments : string " cache_choices has been deprecated and will be removed in Django 1 . 9 . " ,
[PREDICTED]
# call the function warn with 3 arguments : string " cache_choices " has an and 1 and has an 1 " . "

[INPUT]
templatetags_modules_candidates + = [ ' % s . templatetags ' % app_config . name for app_config in apps . get_app_configs ( ) ]
[GROUND TRUTH]
# add string ' % s . templatetags ' to a list , where ' % s ' is replaced with app_config . name ,
[PREDICTED]
# append string ' % s . name ' to a list , append it to a list , append it to a list , append it to a list
```
