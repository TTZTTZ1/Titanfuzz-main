
import torch
tensor = torch.tensor([[1, 2], [3, 4]])
split_size_or_sections = 2
dim = 0
result = tensor.split(split_size_or_sections, dim)
print(result)
