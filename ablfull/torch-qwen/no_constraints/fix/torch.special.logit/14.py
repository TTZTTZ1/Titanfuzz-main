import torch
x = torch.tensor([0.1])
result = torch.special.logit(x)
print(result)