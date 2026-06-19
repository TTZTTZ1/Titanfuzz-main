import torch
tensor = torch.randn(10, 5)
split_size_or_sections = [3, 4, 3]
dim = 0
result = tensor.split(split_size_or_sections, dim)