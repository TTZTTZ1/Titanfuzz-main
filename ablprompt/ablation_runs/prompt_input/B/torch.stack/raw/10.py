import torch

# Create a list of tensors with the same shape
tensors = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]

# Stack them along a new dimension
stacked_tensor = torch.stack(tensors, dim=1)

print(stacked_tensor.shape)  # Output should be (2, 3, 3)