import torch

# Generate input data
tensor = torch.randn(4, 4)
dim = 0

# Call the API
stride = tensor.stride(dim)

print(stride)