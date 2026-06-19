import torch
a = torch.tensor([0.0, 1.0])
b = torch.tensor([4.0, 5.0])
weight = 0.5
result = a.lerp_(b, weight)
print(result)