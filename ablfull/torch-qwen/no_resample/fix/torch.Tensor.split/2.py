import torch
tensor = torch.randn(6)
split_size_or_sections = [2, 2, 2]
result = tensor.split(split_size_or_sections)
print(result)