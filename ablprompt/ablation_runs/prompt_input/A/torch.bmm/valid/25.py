import torch

# Create two 3x3 matrices
matrix1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = torch.tensor([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Perform batch matrix multiplication
result = torch.bmm(matrix1.unsqueeze(0), matrix2.unsqueeze(0))

print(result)