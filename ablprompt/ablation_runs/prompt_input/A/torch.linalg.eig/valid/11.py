import torch

# Create a sample tensor
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)