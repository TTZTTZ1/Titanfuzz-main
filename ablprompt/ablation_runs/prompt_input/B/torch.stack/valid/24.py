import torch

# Create a list of tensors with the same shape
tensors = [torch.randn(4, 5), torch.randn(4, 5), torch.randn(4, 5)]

# Stack the tensors along a new dimension (dim=0)
stacked_tensor = torch.stack(tensors, dim=0)

print(stacked_tensor.shape)  # Output should be (3, 4, 5)