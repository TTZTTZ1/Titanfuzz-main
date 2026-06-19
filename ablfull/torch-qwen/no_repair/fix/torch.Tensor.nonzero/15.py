
import torch
input_tensor = torch.tensor([[1, 0], [0, 2]])
result = input_tensor.nonzero(as_tuple=True)
print(result)
