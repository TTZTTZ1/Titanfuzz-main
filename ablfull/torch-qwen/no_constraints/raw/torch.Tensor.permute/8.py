import torch

# Generate input data
data = torch.randn(2, 3, 4)

# Call the API
permuted_data = data.permute(2, 0, 1)