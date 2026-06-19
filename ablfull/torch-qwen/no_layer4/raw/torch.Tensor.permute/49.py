import torch

# Create a sample tensor
input_tensor = torch.randn(2, 3, 4)

# Permute the dimensions of the tensor
permuted_tensor = input_tensor.permute(2, 0, 1)