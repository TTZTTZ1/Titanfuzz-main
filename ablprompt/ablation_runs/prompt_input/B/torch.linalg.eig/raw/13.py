import torch

# Create a random complex matrix
n = 5
A = torch.randn(n, n, dtype=torch.complex64)

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)