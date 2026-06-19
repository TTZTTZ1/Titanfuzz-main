import torch
matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])
inverse_matrix = torch.linalg.inv(matrix)
print(inverse_matrix)