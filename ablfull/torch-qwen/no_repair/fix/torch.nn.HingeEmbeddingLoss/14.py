
import torch
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'
input1 = torch.randn(3)
input2 = torch.randn(3)
loss = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)(input1, input2)
