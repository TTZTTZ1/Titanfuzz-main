import torch
input_tensor = torch.tensor([[0, 0], [1, 2]])
result = input_tensor.nonzero(as_tuple=True)
print(result)