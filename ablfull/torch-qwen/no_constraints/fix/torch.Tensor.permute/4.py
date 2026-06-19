import torch
input_tensor = torch.randn(3, 4, 5)
permuted_tensor = input_tensor.permute(2, 0, 1)