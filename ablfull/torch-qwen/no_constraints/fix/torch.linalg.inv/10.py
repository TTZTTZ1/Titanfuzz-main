import torch
input_matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]])
inverse_matrix = torch.linalg.inv(input_matrix)
print(inverse_matrix)