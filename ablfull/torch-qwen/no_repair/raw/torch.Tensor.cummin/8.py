import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
dim = 0

# Call the API
result = input_tensor.cummin(dim)

print(result)