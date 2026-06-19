import torch

# Create a sample square matrix
matrix = torch.tensor([[4, 2], [1, 3]], dtype=torch.float64)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)