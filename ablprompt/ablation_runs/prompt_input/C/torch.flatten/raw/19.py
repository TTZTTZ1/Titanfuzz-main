import torch

# Create a 4D tensor
t = torch.randn(2, 3, 4, 5)

# Flatten the tensor from the second dimension to the fourth dimension
flattened_t = torch.flatten(t, start_dim=1, end_dim=3)

print(flattened_t.shape)  # Output should be torch.Size([2, 60]) because 3*4*5 = 60