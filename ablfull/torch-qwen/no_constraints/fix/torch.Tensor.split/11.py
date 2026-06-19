import torch
tensor = torch.randn(10, 5)
split_size = 2
result = tensor.split(split_size, dim=0)
print(result)