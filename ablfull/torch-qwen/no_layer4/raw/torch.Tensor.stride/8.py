import torch

# Prepare valid input data
input_tensor = torch.randn(4, 5)
dim = 0

# Call the API
result = input_tensor.stride(dim)

print(result)