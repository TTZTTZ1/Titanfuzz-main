import torch

# Create a 4D tensor
t = torch.randn(2, 3, 4, 5)

# Flatten dimensions 1 and 2
flattened_tensor = torch.flatten(t, start_dim=1, end_dim=2)

print(flattened_tensor.shape)  # Output should be torch.Size([2, 12, 5])