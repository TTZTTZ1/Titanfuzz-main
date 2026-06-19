
import torch
tensor = torch.randn(2, 3, 4)
dims = (2, 0, 1)
result = tensor.permute(dims)
