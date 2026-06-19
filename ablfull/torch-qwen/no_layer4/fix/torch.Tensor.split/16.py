import torch
input_tensor = torch.randn(10)
split_sizes = [4, 3, 3]
result = input_tensor.split(split_sizes, dim=0)
print(result)