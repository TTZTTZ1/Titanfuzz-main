import torch

# Generate input data
input_tensor = torch.tensor([1, 3, 2])

# Call the API
result = input_tensor.cummin(dim=0)

print(result)