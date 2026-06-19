import torch

# Create a random tensor
A = torch.randn(3, 4, dtype=torch.float)

# Compute the SVD
U, S, Vh = torch.linalg.svd(A, full_matrices=True, driver=None)

print("U:", U)
print("S:", S)
print("Vh:", Vh)