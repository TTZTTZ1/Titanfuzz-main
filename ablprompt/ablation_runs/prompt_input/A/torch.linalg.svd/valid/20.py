import torch

# Create a random matrix
matrix = torch.randn(3, 4)

# Compute the SVD of the matrix
U, s, Vh = torch.linalg.svd(matrix)

print("U:", U)
print("Singular values:", s)
print("Vh:", Vh)