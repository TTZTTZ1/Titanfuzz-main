import torch

# Create a tensor
tensor = torch.randn(2, 3, 4)

# Permute the dimensions
permuted_tensor = tensor.permute(2, 0, 1)