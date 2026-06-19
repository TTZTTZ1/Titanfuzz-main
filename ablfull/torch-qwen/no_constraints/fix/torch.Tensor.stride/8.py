import torch
tensor = torch.randn(3, 4)
stride_result = tensor.stride()
print(stride_result)