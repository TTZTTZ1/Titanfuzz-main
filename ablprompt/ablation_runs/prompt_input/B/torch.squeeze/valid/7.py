import torch

# Create a tensor with some singleton dimensions
x = torch.randn(2, 1, 3, 1, 4)

# Squeeze out all singleton dimensions
y = torch.squeeze(x)

print(y.shape)