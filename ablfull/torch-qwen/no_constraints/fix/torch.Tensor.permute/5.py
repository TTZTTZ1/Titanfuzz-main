import torch
input_tensor = torch.randn(2, 3, 4)
permuted_tensor = input_tensor.permute(2, 0, 1)