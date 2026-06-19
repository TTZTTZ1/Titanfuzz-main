import torch

# Define two matrices: A and B
A = torch.tensor([[3, 1], [1, 2]], dtype=torch.float32)
B = torch.tensor([9, 8], dtype=torch.float32)

# Use torch.linalg.solve to solve the linear system Ax = B
x = torch.linalg.solve(A, B)

print("Solution x:", x)