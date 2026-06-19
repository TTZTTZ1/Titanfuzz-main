import torch
input1 = torch.tensor([1.0])
input2 = torch.tensor([(- 1.0)])
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'
loss_fn = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)
loss = loss_fn(input1, input2)
print(loss)