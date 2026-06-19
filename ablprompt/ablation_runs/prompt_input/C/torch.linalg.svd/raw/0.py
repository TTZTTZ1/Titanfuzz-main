import torch

# Create a random tensor
A = torch.randn(3, 4, device='cuda')

# Compute the SVD
U, S, Vh = torch.linalg.svd(A, full_matrices=False, driver='gesvdj')

print("U:", U)
print("S:", S)
print("Vh:", Vh)