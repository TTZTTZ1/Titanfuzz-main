import torch

# Generate input data
tensor = torch.randn(4, 5)

# Call the API
stride_result = tensor.stride()

print(stride_result)