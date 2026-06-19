import torch

# Create a sample tensor
x = torch.randn(3, 4)

# Flatten the tensor
flattened_x = torch.flatten(x)

print(flattened_x)