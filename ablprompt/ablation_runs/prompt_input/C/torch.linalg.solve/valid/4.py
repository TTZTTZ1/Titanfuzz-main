import torch

# Define a square coefficient matrix A
A = torch.tensor([[3., 1.], [1., 2.]], dtype=torch.float32)

# Define the right-hand side vector B
B = torch.tensor([9., 8.], dtype=torch.float32)

# Solve the system AX = B
X = torch.linalg.solve(A, B)

print("Solution X:", X)