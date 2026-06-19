import torch

# Define two matrices: A (square matrix) and b (right-hand side vector)
A = torch.tensor([[3, 1], [1, 2]], dtype=torch.float32)
b = torch.tensor([9, 8], dtype=torch.float32)

# Use torch.linalg.solve to solve the linear system Ax = b
x = torch.linalg.solve(A, b)

print("Solution x:", x)