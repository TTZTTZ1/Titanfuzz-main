import torch

# Create a random Hermitian matrix
matrix = torch.randn(4, 4, dtype=torch.complex64)
matrix = (matrix + matrix.conj().T) / 2

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)