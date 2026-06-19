import torch

# Create a list of tensors with the same shape
tensors = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]

# Stack the tensors along a new dimension (dim=1)
stacked_tensor = torch.stack(tensors, dim=1)

print(stacked_tensor.shape)  # Output should be (2, 3, 3)