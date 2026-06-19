import torch
a = torch.tensor([1.0], dtype=torch.float32)
b = torch.tensor([1.5], dtype=torch.float32)
result = a.nextafter_(b)