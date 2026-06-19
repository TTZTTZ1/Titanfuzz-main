import torch
input_tensor = torch.randn(3, 4)
dim = 0
stride_result = input_tensor.stride(dim)
print(stride_result)