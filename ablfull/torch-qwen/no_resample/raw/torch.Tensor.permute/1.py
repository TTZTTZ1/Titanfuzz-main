import torch

# Create a tensor
tensor = torch.randn(2, 3, 4)

# Permute dimensions
permuted_tensor = tensor.permute(2, 0, 1)