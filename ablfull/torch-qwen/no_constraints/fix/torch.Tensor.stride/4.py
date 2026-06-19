import torch
tensor = torch.randn(4, 4)
stride_result = tensor.stride()
print(stride_result)