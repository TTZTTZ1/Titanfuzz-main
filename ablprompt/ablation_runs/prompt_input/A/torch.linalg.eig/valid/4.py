import torch

# Create a random complex matrix
matrix = torch.randn(4, 4, dtype=torch.complex64)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)