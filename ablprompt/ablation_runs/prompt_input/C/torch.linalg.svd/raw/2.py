import torch

# Create a random tensor of size (3, 4)
A = torch.randn(3, 4)

# Compute the Singular Value Decomposition
U, S, Vh = torch.linalg.svd(A, full_matrices=True, driver=None)

print("U:", U)
print("S:", S)
print("Vh:", Vh)