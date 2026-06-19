import torch
tensor = torch.randn(10)
split_size_or_sections = [2, 4, 4]
result = tensor.split(split_size_or_sections)
print(result)