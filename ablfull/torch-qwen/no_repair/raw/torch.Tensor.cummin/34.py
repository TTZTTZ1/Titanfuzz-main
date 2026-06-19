import torch

# Generate input data
input_tensor = torch.tensor([3, 1, 4, 1, 5, 9])

# Call the API
result = torch.Tensor.cummin(input_tensor, dim=0)

print(result)