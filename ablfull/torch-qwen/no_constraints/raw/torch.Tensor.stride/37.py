import torch

# Generate input data
input_tensor = torch.randn(4, 5)

# Call the API
stride_result = input_tensor.stride()

print(stride_result)