import torch
x = torch.tensor([(- 0.5), 0.0, 0.5, 1.5])
result = torch.fix(x)
print(result)