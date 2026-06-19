import torch

# Create a random complex matrix
A = torch.randn(3, 3, dtype=torch.complex64)

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)