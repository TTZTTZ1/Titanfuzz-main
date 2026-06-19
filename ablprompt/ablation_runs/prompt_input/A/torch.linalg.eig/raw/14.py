import torch

# Create a sample tensor for eigenvalue decomposition
A = torch.tensor([[4, 2], [1, 3]], dtype=torch.float64)

# Call the torch.linalg.eig function
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)