import torch
tensor = torch.tensor([[1, 0], [0, 2]])
result = tensor.nonzero()
print(result)