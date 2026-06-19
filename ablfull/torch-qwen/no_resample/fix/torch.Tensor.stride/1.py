import torch
tensor = torch.randn(4, 4)
stride = tensor.stride()
print(stride)