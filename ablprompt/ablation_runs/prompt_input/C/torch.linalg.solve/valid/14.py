import torch

# Define a 3x3 matrix A and a 3x1 vector B
A = torch.tensor([[3., 1., 2.], [2., -2., 4.], [-1., 0.5, -1.]], dtype=torch.double)
B = torch.tensor([1., -2., 0.], dtype=torch.double)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)