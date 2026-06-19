import torch

# Create a tensor
tensor = torch.randn(2, 3)

# Permute the dimensions to be reversed
permuted_tensor = tensor.permute(1, 0)