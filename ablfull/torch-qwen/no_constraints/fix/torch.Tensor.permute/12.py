import torch
tensor = torch.randn(4, 3, 2)
permuted_tensor = tensor.permute(2, 0, 1)