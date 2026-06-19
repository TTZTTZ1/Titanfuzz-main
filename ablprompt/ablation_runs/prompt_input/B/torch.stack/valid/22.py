import torch

# Create a list of tensors
tensors = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]

# Stack the tensors along a new dimension (dim=0)
stacked_tensor = torch.stack(tensors, dim=0)

print(stacked_tensor.shape)  # Output should be (3, 2, 3)