import torch

# Create a sample square matrix
matrix = torch.tensor([[4, 2], [1, 3]], dtype=torch.float32)

# Compute eigenvalues and eigenvectors using torch.linalg.eig
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)