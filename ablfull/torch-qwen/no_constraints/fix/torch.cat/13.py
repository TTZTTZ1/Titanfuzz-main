import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
result = torch.cat((x, y), dim=0)
print(result)