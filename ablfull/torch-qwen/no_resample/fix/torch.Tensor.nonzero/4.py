import torch
tensor = torch.tensor([[0, 0], [0, 1]])
result = tensor.nonzero(as_tuple=True)
print(result)