import torch

# Generate two 2x3 matrices as input data
matrix1 = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
matrix2 = torch.tensor([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])

# Call the API torch.bmm
result = torch.bmm(matrix1.unsqueeze(0), matrix2.unsqueeze(0)).squeeze(0)

print(result)