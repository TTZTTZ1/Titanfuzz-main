import torch

# Create a random tensor
x = torch.randn(3, 4)

# Apply sigmoid activation
y = torch.sigmoid(x)

print(y)