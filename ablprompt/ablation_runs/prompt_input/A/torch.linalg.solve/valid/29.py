import torch

# Define two matrices: A (square matrix) and b (right-hand side vector)
A = torch.tensor([[3, 1], [1, 2]], dtype=torch.float32)
b = torch.tensor([9, 8], dtype=torch.float32)

# Solve the linear system Ax = b using torch.linalg.solve
x = torch.linalg.solve(A, b)

print("Solution x:", x)