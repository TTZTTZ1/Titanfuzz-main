import torch

# Create a random tensor
t = torch.randn(3, 4, 5)

# Flatten the tensor from the second dimension to the last dimension
flattened_tensor = torch.flatten(t, start_dim=1)

print(flattened_tensor)