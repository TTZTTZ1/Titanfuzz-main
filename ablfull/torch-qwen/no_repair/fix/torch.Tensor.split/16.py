
import torch
tensor = torch.randn(10)
split_size_or_sections = [3, 3, 4]
dim = 0
result = tensor.split(split_size_or_sections, dim)
