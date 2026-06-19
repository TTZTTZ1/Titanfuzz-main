import torch

# Prepare input data
input1 = torch.tensor([1.0])
input2 = torch.tensor([-1.0])
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)
output = loss_fn(input1, input2)

print(output)