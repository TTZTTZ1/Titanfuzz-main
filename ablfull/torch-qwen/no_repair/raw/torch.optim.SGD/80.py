import torch

# Generate a dummy tensor
param = torch.randn(3, requires_grad=True)

# Initialize SGD optimizer with nesterov set to False and momentum set to 0.9
optimizer = torch.optim.SGD([param], lr=0.01, momentum=0.9)