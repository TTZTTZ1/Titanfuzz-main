import torch

# Create a random Hermitian matrix
n = 4
A = torch.randn(n, n, dtype=torch.cfloat)
A = A + A.conj().T  # Ensure it's Hermitian

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)