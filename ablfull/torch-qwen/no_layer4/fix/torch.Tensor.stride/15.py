import torch
tensor = torch.randn(4, 5)
stride = tensor.stride()
print(stride)