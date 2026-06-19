
import torch
tensor = torch.randn(10, 5)
split_size_or_sections = [4, 6]
dim = 0
result = tensor.split(split_size_or_sections, dim)
