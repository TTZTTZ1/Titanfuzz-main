import torch

# Create a tensor with an extra dimension of size 1
x = torch.randn(2, 1, 3)

# Squeeze out the single-dimensional entries from the shape of x
y = torch.squeeze(x)

print(y)