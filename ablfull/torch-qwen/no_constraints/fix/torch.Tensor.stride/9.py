import torch
input_tensor = torch.randn(3, 4)
stride_result = input_tensor.stride()
print(stride_result)