import torch

# Prepare valid input data
tensor = torch.randn(10, 4)  # A tensor of size 10x4
split_size = 5

# Call the API
result = tensor.split(split_size)

print(result)