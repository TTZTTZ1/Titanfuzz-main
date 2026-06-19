import torch

a = torch.randn(10, 3, 4)
split_sizes = [2, 3, 5]
result = torch.split(a, split_sizes, dim=1)
print(result)