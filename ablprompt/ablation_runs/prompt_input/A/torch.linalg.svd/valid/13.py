import torch

# Create a sample tensor
matrix = torch.tensor([[1., 2.], [3., 4.]])

# Perform SVD decomposition
U, s, Vh = torch.linalg.svd(matrix)

print("U:", U)
print("Singular values:", s)
print("Vh:", Vh)