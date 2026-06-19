import torch
input_tensor = torch.tensor([[0, 0, 1], [1, 0, 2]])
result = input_tensor.nonzero()
print(result)