import torch

# Create a random Hermitian matrix
n = 5
A = torch.randn(n, n, dtype=torch.cfloat)
A = A + A.conj().T

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)