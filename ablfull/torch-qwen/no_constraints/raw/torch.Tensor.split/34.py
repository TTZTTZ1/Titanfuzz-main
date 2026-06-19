import torch

# Generate input data
tensor = torch.randn(10)
split_size = 5

# Call the API
result = tensor.split(split_size)

print(result)