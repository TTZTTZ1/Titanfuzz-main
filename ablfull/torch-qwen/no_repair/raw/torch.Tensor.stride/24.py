import torch

# Prepare valid input data
tensor = torch.randn(3, 4)
dim = 0

# Call the API
stride_result = tensor.stride((dim,))
print(stride_result)