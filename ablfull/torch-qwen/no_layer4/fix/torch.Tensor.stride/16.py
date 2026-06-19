import torch
tensor = torch.randn(3, 4)
dim = 0
stride = tensor.stride(dim)