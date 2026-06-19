import torch

# Create a tensor with some singleton dimensions
x = torch.randn(1, 3, 4, 1)

# Squeeze out the singleton dimensions
y = torch.squeeze(x)

print("Original tensor shape:", x.shape)
print("Squeezed tensor shape:", y.shape)