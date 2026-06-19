import torch

# Prepare input data
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
dim = 0

# Call the API
result = input_tensor.cummin(dim)