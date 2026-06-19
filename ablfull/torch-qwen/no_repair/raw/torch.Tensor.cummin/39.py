import torch

# Generate input data
input_tensor = torch.tensor([[4.0, 2.0], [3.0, 5.0]])

# Call the API
result = torch.Tensor.cummin(input_tensor, dim=1)

print(result)