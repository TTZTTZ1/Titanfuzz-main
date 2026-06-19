import torch
input_data = torch.tensor([[0, 1], [2, 0]])
result = input_data.nonzero()
print(result)