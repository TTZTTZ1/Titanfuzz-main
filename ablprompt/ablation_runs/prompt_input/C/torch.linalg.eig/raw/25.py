import torch

# Create a random complex tensor
n = 5
A = torch.randn(n, n, dtype=torch.cfloat)

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)