import torch
input_tensor = torch.tensor([[0, 1, 0], [2, 0, 3]])
result = input_tensor.nonzero(as_tuple=True)
print(result)