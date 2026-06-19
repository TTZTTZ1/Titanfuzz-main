import torch

# Generate input data
input_tensor = torch.randn(2, 3, 4)

# Call the API
permuted_tensor = input_tensor.permute(2, 0, 1)