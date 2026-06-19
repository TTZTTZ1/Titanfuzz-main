import torch
x = torch.tensor([0.1, 0.4, 0.6, 0.9])
result = torch.special.logit(x)
print(result)