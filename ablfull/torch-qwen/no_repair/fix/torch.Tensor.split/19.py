
import torch
tensor = torch.randn(6, 4)
split_sizes = [2, 2, 2]
result = tensor.split(split_sizes)
print(result)
