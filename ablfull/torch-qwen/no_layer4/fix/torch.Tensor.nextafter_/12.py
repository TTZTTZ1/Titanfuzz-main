import torch
x = torch.tensor([1.0], dtype=torch.float32)
y = torch.tensor(2.0, dtype=torch.float32)
result = x.nextafter_(y)