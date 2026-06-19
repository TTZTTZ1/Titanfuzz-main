import torch
tensor = torch.randn(4, 5)
stride_result = tensor.stride()
print(stride_result)