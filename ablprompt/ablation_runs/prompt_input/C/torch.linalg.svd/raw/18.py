import torch

# Create a random matrix
A = torch.randn(3, 4, device='cuda')

# Compute SVD
U, S, Vh = torch.linalg.svd(A, full_matrices=False)

print("U:", U)
print("S:", S)
print("Vh:", Vh)