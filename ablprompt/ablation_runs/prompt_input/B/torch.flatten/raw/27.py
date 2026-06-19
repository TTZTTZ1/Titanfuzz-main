import torch

# Create a random tensor
t = torch.randn(2, 3, 4)

# Flatten the tensor from the second dimension to the last dimension
flattened_t = torch.flatten(t, start_dim=1)

print(flattened_t)