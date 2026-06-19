import torch

# Create a sample tensor
A = torch.tensor([[1., 2.], [3., 4.]])

# Compute the SVD of A
U, s, Vh = torch.linalg.svd(A)

print("U:", U)
print("s:", s)
print("Vh:", Vh)