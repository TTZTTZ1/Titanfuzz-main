
import torch
tensor = torch.randn(4, 5)
dim = 0
stride_result = tensor.stride(dim)
print(stride_result)
