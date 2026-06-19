import torch

# Create a sample tensor
tensor = torch.tensor([[1., 2.], [3., 4.]])

# Compute SVD
U, s, Vh = torch.linalg.svd(tensor)

print("U:", U)
print("Singular values:", s)
print("Vh:", Vh)