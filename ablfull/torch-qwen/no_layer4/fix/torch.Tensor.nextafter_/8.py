import torch
self_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
other_tensor = torch.tensor([1.5, 2.5, 3.5], dtype=torch.float32)
result = self_tensor.nextafter_(other_tensor)
print(result)