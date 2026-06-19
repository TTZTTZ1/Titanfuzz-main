import torch

# Create a random matrix
matrix = torch.randn(3, 4)

# Compute SVD
U, S, Vh = torch.linalg.svd(matrix)

print("U:", U)
print("S:", S)
print("Vh:", Vh)