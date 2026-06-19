
import torch
tensor = torch.randn(4, 4)
split_size_or_sections = [2, 2]
dim = 0
result = tensor.split(split_size_or_sections, dim)
print(result)
