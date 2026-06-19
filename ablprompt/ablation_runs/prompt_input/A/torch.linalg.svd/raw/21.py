import torch

# Create a sample tensor
matrix = torch.tensor([[1., 2.], [3., 4.]])

# Compute SVD
U, S, Vh = torch.linalg.svd(matrix)

print("U:", U)
print("S:", S)
print("Vh:", Vh)