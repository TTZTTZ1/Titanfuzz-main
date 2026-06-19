import torch
x = torch.tensor([(- 1.5), 0.2, 3.7])
result = torch.fix(x)
print(result)