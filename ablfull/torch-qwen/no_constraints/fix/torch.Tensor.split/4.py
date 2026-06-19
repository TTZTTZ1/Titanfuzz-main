import torch
tensor = torch.randn(10)
split_size = 5
result = tensor.split(split_size)
print(result)