import torch
input_tensor = torch.randn(4, 5)
split_size_or_sections = [2, 2]
dim = 0
result = input_tensor.split(split_size_or_sections, dim)