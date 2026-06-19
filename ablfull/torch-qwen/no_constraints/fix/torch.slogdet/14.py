import torch
matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])
result = torch.slogdet(matrix)
print(result)