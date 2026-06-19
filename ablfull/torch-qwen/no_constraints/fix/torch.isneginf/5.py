import torch
x = torch.tensor((- float('inf')))
result = torch.isneginf(x)
print(result)