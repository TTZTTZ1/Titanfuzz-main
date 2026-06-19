import torch

# Create a sample matrix
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Compute SVD
U, s, Vh = torch.linalg.svd(matrix)

print("U:", U)
print("Singular values:", s)
print("Vh:", Vh)