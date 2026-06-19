import torch

# Prepare valid input data
tensor = torch.randn(4, 5)
dim = 0

# Call the target API
stride_result = tensor.stride((dim,))
print(stride_result)