
import torch
self_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_tensor = torch.tensor([1.1, 2.2], dtype=torch.float32)
result = self_tensor.nextafter_(other_tensor)
