
import torch
tensor = torch.randn(2, 3)
dims = (1, 0)
result = tensor.permute(dims)
