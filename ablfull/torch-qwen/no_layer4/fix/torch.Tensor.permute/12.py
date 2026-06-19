import torch
input_tensor = torch.randn(3, 4)
dims = (1, 0)
result = input_tensor.permute(dims)