import torch

# Create a random tensor with shape (2, 3, 4)
t = torch.randn(2, 3, 4)

# Flatten the tensor from dimension 1 to dimension 2
flattened_t = torch.flatten(t, start_dim=1, end_dim=2)

print(flattened_t.shape)  # Output should be torch.Size([2, 12])