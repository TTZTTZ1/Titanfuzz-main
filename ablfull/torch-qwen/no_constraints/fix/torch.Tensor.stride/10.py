import torch
data = torch.randn(3, 4)
stride_result = data.stride()
print(stride_result)