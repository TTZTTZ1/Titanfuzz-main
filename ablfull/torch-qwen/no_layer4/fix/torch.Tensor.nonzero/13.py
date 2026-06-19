import torch
tensor = torch.tensor([[1, 0], [0, 2]])
result = tensor.nonzero(as_tuple=True)
print(result)