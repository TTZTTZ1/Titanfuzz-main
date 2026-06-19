import torch

# Create a sample matrix
A = torch.tensor([[4, 2], [1, 3]], dtype=torch.float64)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)