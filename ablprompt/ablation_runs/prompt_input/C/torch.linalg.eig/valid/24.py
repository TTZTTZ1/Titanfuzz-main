import torch

# Create a random Hermitian matrix
n = 5
A = torch.randn(n, n, dtype=torch.cfloat)
A = A + A.conj().t()  # Ensure A is Hermitian

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)