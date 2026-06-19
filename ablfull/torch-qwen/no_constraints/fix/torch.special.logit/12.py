import torch
x = torch.tensor([(- 0.5), 0.0, 0.5])
result = torch.special.logit(x)
print(result)