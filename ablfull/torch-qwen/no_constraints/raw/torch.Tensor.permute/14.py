import torch

# Generate input data
tensor = torch.randn(2, 3)

# Call the API
permuted_tensor = tensor.permute(1, 0)