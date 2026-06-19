
import torch
tensor = torch.randn(2, 3, 4)
dims = (1, 0, 2)
result = tensor.permute(dims)
