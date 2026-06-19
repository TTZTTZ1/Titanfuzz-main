import torch

# Create a tensor
tensor = torch.randn(2, 3)

# Permute dimensions
permuted_tensor = tensor.permute(1, 0)