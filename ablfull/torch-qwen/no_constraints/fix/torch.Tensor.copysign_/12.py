import torch
a = torch.tensor([(- 1.0), (- 2.0), 3.0])
b = torch.tensor([1.0, (- 1.0), (- 1.0)])
result = a.copysign_(b)
print(result)