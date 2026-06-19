import torch

# Create a list of tensors with the same shape
tensors = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]

# Stack them along a new dimension (dim=0)
stacked_tensor = torch.stack(tensors, dim=0)

print(stacked_tensor.shape)  # Output should be (3, 2, 3)