import torch

# Create a random matrix
matrix = torch.randn(4, 4)

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)