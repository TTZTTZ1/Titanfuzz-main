import torch
tensor = torch.randn(2, 3)
dims = (1, 0)
permuted_tensor = tensor.permute(dims)