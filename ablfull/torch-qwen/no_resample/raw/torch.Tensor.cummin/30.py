import torch

# Generate input data
input_tensor = torch.tensor([3, 1, 4, 1, 5], dtype=torch.float32)

# Call the API
result = input_tensor.cummin(dim=0)
print(result)