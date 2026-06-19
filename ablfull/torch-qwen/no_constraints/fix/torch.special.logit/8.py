import torch
x = torch.tensor([0.5, 0.7])
result = torch.special.logit(x)
print(result)