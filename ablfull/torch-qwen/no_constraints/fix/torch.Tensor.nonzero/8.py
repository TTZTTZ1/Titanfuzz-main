import torch
input_tensor = torch.tensor([[0, 0, 0], [0, 1, 0], [1, 0, 0]])
result = input_tensor.nonzero()
print(result)