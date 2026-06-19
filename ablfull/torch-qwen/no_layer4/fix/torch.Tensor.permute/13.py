import torch
tensor = torch.randn(2, 3, 4)
dims = (1, 0, 2)
permuted_tensor = tensor.permute(dims)