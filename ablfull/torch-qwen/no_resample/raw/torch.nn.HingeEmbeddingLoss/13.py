import torch

# Prepare input data
input1 = torch.randn(3)
input2 = torch.randn(3)
target = torch.randint(0, 2, (3,))
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'

# Call the API
loss = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)(input1, input2, target)
print(loss.item())