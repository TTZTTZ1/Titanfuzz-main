import torch

# Define two matrices: A (square) and b (column vector)
A = torch.tensor([[3, 1], [1, 2]], dtype=torch.float32)
b = torch.tensor([9, 8], dtype=torch.float32)

# Solve the linear system Ax = b
x = torch.linalg.solve(A, b)

print("Solution x:", x)