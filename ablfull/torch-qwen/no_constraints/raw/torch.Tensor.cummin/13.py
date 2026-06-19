import torch

# Generate input data
input_tensor = torch.tensor([[7, 2], [5, 6]])

# Call the API
result = input_tensor.cummin(dim=0)

print(result)