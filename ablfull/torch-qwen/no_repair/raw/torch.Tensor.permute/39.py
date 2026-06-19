import torch

# Prepare valid input data
tensor = torch.randn(2, 3, 4)
dims = (2, 0, 1)

# Call the API
result = tensor.permute(dims)
print(result)