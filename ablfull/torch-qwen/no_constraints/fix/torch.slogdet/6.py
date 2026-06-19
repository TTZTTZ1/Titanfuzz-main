import torch
input_matrix = torch.tensor([[4.0, 0.0], [0.0, 3.0]])
result = torch.slogdet(input_matrix)
print(result)