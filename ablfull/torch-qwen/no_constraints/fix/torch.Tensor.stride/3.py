import torch
data = torch.randn(4, 4)
stride_result = data.stride()
print(stride_result)