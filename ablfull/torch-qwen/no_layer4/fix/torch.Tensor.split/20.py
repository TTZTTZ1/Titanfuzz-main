import torch
tensor = torch.randn(10, 5)
split_size = [2, 3, 5]
dim = 0
result = tensor.split(split_size, dim)