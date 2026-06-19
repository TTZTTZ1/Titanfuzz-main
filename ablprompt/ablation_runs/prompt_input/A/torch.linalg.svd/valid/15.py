import torch

# Create a sample matrix
A = torch.tensor([[1., 2.], [3., 4.]])

# Compute SVD
U, s, Vh = torch.linalg.svd(A)

print("U:", U)
print("Singular values:", s)
print("Vh:", Vh)