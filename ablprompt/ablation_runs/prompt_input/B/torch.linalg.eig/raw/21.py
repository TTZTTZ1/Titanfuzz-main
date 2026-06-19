import torch

# Create a random complex matrix
n = 4
A = torch.randn(n, n, dtype=torch.cfloat)

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.linalg.eig(A)

# Print the results
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)