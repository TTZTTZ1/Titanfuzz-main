import torch

# Create a sample matrix
matrix = torch.tensor([[1., 2.], [3., 4.]])

# Compute SVD
U, s, Vh = torch.linalg.svd(matrix)

print("U:", U)
print("Singular values:", s)
print("Vh:", Vh)