import torch
x = torch.tensor([False, False, True])
result = torch.any(x)
print(result)