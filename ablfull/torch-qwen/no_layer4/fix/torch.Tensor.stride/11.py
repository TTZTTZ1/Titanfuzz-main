import torch
tensor = torch.randn(4, 4)
dim = 0
stride = tensor.stride(dim)
print(stride)