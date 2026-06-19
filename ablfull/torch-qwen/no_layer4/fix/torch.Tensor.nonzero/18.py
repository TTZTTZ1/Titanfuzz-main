import torch
data = torch.tensor([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
result = data.nonzero(as_tuple=True)
print(result)