import torch
input_tensor = torch.randn(2, 3, 4)
dims = (2, 0, 1)
permuted_tensor = input_tensor.permute(dims)