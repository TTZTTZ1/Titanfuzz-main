import torch
x = torch.tensor([(- 1.5), (- 0.4), 0.3, 1.7])
result = torch.special.round(x)
print(result)