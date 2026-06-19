import torch
input_data = torch.tensor([[0, 1, 0], [2, 0, 3]])
result = input_data.nonzero()
print(result)