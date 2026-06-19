import torch

# Create a random complex tensor
A = torch.randn(3, 3, dtype=torch.cfloat)

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)