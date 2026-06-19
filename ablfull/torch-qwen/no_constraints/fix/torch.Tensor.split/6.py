import torch
tensor = torch.randn(10)
split_size = 5
dim = 0
result = tensor.split(split_size, dim)