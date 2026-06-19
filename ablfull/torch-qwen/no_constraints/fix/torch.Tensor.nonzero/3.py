import torch
input_tensor = torch.tensor([[0, 1], [2, 0]], dtype=torch.int)
result = input_tensor.nonzero()
print(result)