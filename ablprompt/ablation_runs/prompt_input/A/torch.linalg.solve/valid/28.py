import torch

# Create two matrices, A and B
A = torch.tensor([[3., 1.], [1., 2.]])
B = torch.tensor([9., 8.])

# Solve the linear system Ax = B for x
x = torch.linalg.solve(A, B)

print(x)