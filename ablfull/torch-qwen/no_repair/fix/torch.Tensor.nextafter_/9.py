
import torch
self_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_tensor = torch.tensor([1.1, 2.2], dtype=torch.float32)
result = torch.Tensor.nextafter_(self_tensor, other_tensor)
print(result)
