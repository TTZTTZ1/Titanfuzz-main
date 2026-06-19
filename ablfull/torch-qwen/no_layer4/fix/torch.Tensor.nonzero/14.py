import torch
tensor = torch.tensor([0, 1, 0, 2, 0])
result = tensor.nonzero(as_tuple=True)
print(result)