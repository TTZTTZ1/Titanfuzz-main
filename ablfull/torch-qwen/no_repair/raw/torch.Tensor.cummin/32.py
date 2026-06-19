import torch

# Generate input data
input_tensor = torch.tensor([[1, 2], [4, 3]])

# Call the API
result = input_tensor.cummin(dim=1)