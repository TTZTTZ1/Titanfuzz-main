import torch

# Generate input data
tensor = torch.randn(4, 4)

# Call the API
stride = tensor.stride()

print(stride)