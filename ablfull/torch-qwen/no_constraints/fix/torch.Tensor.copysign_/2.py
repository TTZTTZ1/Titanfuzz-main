import torch
x = torch.tensor([(- 1.0), (- 2.0), 3.0])
y = torch.tensor([1.0, (- 2.0), 3.0])
result = x.copysign_(y)
print(result)