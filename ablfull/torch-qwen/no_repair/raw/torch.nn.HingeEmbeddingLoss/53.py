import torch

# Prepare valid input data
margin = 1.0
size_average = True
reduce = True
input1 = torch.tensor([-1.0], requires_grad=True)
input2 = torch.tensor([1.0], requires_grad=True)

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction='mean')
loss = loss_fn(input1, input2)

print(loss)