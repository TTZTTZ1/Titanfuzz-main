import torch

# Create a tensor
x = torch.randn(3, 4)

# Use torch.unsqueeze to add an extra dimension at index 0
y = torch.unsqueeze(x, 0)

print(y.shape)  # Output should be torch.Size([1, 3, 4])