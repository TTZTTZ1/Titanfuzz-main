import torch

# Create a random matrix
A = torch.randn(3, 4)

# Compute SVD
U, S, Vh = torch.linalg.svd(A)

print("U:", U)
print("S:", S)
print("Vh:", Vh)