import torch
input_tensor = torch.tensor([[0, 2, 0], [3, 0, 5]])
result = input_tensor.nonzero()
print(result)