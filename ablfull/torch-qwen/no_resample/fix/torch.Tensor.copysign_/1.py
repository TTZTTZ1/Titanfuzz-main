import torch
self_tensor = torch.tensor([(- 1.0), 2.0, (- 3.0)], dtype=torch.float32)
other_tensor = torch.tensor([1.0, (- 2.0), 3.0], dtype=torch.float32)
result = self_tensor.copysign_(other_tensor)
print(result)