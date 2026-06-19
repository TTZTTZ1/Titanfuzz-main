import torch

# Prepare input data
tensor = torch.randn(4, 5)
dim = 0

# Call the API
result = tensor.stride(dim)

print(result)