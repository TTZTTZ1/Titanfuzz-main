import torch

# Generate valid input data
input_tensor = torch.tensor([[7, 2, 5], [6, 3, 4]])

# Call the API
result = input_tensor.cummin(dim=1)
print(result)