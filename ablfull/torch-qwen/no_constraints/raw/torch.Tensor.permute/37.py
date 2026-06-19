import torch

# Generate input data
tensor = torch.randn(4, 3, 2)

# Call the API
permuted_tensor = tensor.permute(2, 0, 1)