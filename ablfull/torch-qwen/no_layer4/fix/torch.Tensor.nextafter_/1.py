import torch
a = torch.tensor([1.0], dtype=torch.float32)
b = torch.tensor([2.0], dtype=torch.float32)
result = a.nextafter_(b)
print(result)