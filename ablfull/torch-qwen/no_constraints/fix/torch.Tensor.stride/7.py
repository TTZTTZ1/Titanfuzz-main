import torch
input_tensor = torch.randn(4, 5)
stride_result = input_tensor.stride()
print(stride_result)