import torch
data = torch.tensor([[1, 0], [0, 2]])
result = data.nonzero(as_tuple=True)