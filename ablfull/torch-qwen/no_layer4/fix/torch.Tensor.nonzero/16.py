import torch
data = torch.tensor([0, 0, 1, 0, 2])
result = data.nonzero(as_tuple=True)