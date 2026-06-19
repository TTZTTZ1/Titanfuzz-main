import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute SVD
U, S, Vh = torch.linalg.svd(A, full_matrices=False, driver='gesvd')

print("U:", U)
print("S:", S)
print("Vh:", Vh)