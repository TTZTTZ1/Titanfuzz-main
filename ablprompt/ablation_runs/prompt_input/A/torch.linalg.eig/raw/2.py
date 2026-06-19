import torch

# Create a random Hermitian matrix
A = torch.randn(3, 3, dtype=torch.complex64)
A = A + A.conj().t()

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)