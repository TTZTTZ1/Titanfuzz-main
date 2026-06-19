import torch

# Create a random tensor A with shape (3, 4)
A = torch.randn(3, 4)

# Compute the SVD of A
U, S, Vh = torch.linalg.svd(A, full_matrices=False)

print("U:", U)
print("S:", S)
print("Vh:", Vh)