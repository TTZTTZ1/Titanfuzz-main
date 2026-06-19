
import torch
tensor = torch.randn(2, 3, 4)
dims = (1, 2, 0)
result = tensor.permute(dims)
