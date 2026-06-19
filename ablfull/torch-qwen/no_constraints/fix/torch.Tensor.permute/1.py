import torch
input_tensor = torch.randn(3, 4)
permuted_tensor = input_tensor.permute(1, 0)