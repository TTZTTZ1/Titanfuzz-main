import torch
x = torch.tensor([[1.0], [2.0]])
y = torch.tensor([[3.0], [4.0]])
result = torch.cat((x, y), dim=0)