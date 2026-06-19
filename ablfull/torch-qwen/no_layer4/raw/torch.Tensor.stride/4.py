import torch

# Prepare valid input data
tensor = torch.randn(4, 4)
dim = 0

# Call the API
result = tensor.stride(dim)

print(result)