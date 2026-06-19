import torch
tensor = torch.randn(5, 5)
split_size = 2
dim = 0
result = tensor.split(split_size, dim)