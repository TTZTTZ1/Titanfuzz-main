import torch

# Create a sample tensor
A = torch.tensor([[1., 2.], [3., 4.]])

# Compute SVD
U, s, Vh = torch.linalg.svd(A)

print("U:", U)
print("S:", s)
print("Vh:", Vh)