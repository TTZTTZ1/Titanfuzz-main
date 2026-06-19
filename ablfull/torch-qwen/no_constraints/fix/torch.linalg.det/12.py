import torch
input_matrix = ((torch.rand(3, 3) * 20) - 10)
determinant = torch.linalg.det(input_matrix)