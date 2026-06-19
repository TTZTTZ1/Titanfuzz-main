import torch

# Generate input data
input_tensor = torch.randn(3, 4)

# Call the API
permuted_tensor = input_tensor.permute(1, 0)