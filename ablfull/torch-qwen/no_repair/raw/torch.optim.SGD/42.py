import torch

# Generate dummy parameters
params = [torch.randn(3, requires_grad=True), torch.randn(4, requires_grad=True)]

# Initialize optimizer with valid arguments
optimizer = torch.optim.SGD(params, lr=0.01, momentum=0.9)