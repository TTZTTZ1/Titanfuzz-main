import torch
tensor = torch.randn(2, 3, 4)
dims = (0, 2, 1)
result = tensor.permute(dims)