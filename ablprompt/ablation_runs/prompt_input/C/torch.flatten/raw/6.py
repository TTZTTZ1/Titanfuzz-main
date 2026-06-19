import torch

# Create a 3D tensor
t = torch.randn(2, 3, 4)

# Flatten the tensor from the second dimension to the third dimension
flattened_t = torch.flatten(t, start_dim=1, end_dim=2)

print(flattened_t.shape)  # Output should be torch.Size([2, 12])