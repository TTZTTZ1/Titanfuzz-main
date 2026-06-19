import torch
x = torch.tensor([(- 1.0), (- 2.0)], dtype=torch.float32)
y = torch.tensor([2.0, (- 3.0)], dtype=torch.float32)
x.copysign_(y)