import torch

# Create some dummy parameters
params = [torch.randn(3), torch.randn(4)]

# Initialize SGD optimizer
optimizer = torch.optim.SGD(params, lr=0.01, momentum=0.9)