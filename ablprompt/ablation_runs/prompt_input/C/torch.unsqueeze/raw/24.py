import torch

# Create a random tensor
x = torch.randn(3, 4)

# Insert a new dimension at index 0
y = x.unsqueeze(0)

print(y.shape)  # Output should be [1, 3, 4]