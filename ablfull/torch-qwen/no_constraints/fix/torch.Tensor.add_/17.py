import torch
tensor = torch.tensor([1.0])
other = torch.tensor([2.0])
result = tensor.add_(other)
print(result)