import torch
input_tensor = torch.randn(4, 3, 2)
permuted_tensor = input_tensor.permute(2, 0, 1)