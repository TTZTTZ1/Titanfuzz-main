import torch
input_tensor = torch.randn(5, 3)
stride_result = input_tensor.stride()
print(stride_result)