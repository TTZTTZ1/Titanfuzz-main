import torch

# Prepare input data
tensor = torch.randn(5)
dim = 0  # Scalar integer value

# Call the API
result = tensor.stride(dim)

print(result)