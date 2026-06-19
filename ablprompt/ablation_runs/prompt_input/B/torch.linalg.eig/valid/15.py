import torch

# Create a random complex matrix
matrix = torch.randn(3, 3, dtype=torch.cfloat)

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)