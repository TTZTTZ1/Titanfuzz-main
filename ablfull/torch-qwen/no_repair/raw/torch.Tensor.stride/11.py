import torch

# Generate input data
tensor = torch.randn(3, 4)

# Call the API
result = tensor.stride()
print(result)