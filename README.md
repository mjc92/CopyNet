# Incorporating Copying Mechanism in Sequence-to-Sequence Learning

## Abstract

> We address an important problem in sequence-to-sequence (Seq2Seq) learning referred to as copying, in which certain segments in the input sequence are selectively replicated in the output sequence. A similar phenomenon is observable in human language communication. For example, humans tend to repeat entity names or even long phrases in conversation. The challenge with regard to copying in Seq2Seq is that new machinery is needed to decide when to perform the operation. In this paper, we incorporate copying into neural network-based Seq2Seq learning and propose a new model called CopyNet with encoder-decoder structure. CopyNet can nicely integrate the regular way of word generation in the decoder with the new copying mechanism which can choose sub-sequences in the input sequence and put them at proper places in the output sequence. Our empirical study on both synthetic data sets and real world data sets demonstrates the efficacy of CopyNet. For example, CopyNet can outperform regular RNN-based model with remarkable margins on text summarization tasks.

## About

A PyTorch implementation of Max-Margin Object Detection by Kenta Iwasaki. The original paper author is Davis E. King.

## Observations & Results

To be tested; implementation is almost finished.

## Dataset Preparation

Labels for the model should be represented as a 3D array that follows the shape (num. images, num. labels per image, 5) where the final dimension represents label attributes `(left, top, right, bottom, class)`.
Images for the model should be represented as a 4D array that follows the shape (num. images, 256, 256, 3). Image specifications may easily be changed later, especially after spatial pyramid pooling is implemented to allow for variable length images.

## How To Run

```
pip install http://download.pytorch.org/whl/cu80/torch-0.1.12.post2-cp35-cp35m-linux_x86_64.whl
pip install torchvision
python model.py
```

## Citations

King, D. E. (2015). Max-margin object detection. arXiv preprint arXiv:1502.00046.
