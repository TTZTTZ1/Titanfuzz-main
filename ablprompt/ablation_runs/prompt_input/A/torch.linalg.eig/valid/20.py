import torch

# Create a sample Hermitian matrix
matrix = torch.tensor([[4, 2+1j], [2-1j, 3]], dtype=torch.complex64)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)