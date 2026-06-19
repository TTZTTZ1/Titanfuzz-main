import torch
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,))
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'
loss_fn = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)