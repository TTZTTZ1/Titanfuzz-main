import torch

# Prepare valid input data
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'
input1 = torch.randn(1, requires_grad=True)
input2 = torch.randn(1, requires_grad=True)

# Call the API
loss = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)(input1, input2, torch.ones_like(input1))