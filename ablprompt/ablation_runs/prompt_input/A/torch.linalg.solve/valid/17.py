import torch

# Define two matrices: A (square) and B (right-hand side)
A = torch.tensor([[3, 1], [1, 2]], dtype=torch.float32)
B = torch.tensor([9, 8], dtype=torch.float32)

# Solve the linear system Ax = B for x
x = torch.linalg.solve(A, B)

print("Solution x:", x)