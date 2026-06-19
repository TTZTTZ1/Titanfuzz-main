import torch

# Create a batch of 2x2 matrices A
A = torch.tensor([[[4.0, 7.0], [2.0, 6.0]], [[1.0, 2.0], [3.0, 4.0]]], dtype=torch.float64)

# Create a batch of right-hand side vectors B
B = torch.tensor([[[2.0, 6.0], [2.0, -2.0]], [[1.0, 2.0], [0.0, 1.0]]], dtype=torch.float64)

# Solve AX = B for each batch element
X = torch.linalg.solve(A, B)

print(X)