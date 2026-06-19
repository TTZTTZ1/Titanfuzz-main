import torch

# Generate input data
tensor = torch.randn(10, 5)
split_size = 2

# Call the API
result = tensor.split(split_size, dim=1)

print(result)