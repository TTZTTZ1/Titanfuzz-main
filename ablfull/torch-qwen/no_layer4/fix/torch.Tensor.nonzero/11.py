import torch
input_tensor = torch.tensor([[0, 2], [3, 0]])
result = input_tensor.nonzero(as_tuple=True)
print(result)