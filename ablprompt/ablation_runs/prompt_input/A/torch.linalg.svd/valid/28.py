import torch

# Create a sample tensor
tensor = torch.tensor([[1., 2.], [3., 4.]])

# Compute the Singular Value Decomposition (SVD)
U, S, Vh = torch.linalg.svd(tensor)

print("U:", U)
print("S:", S)
print("Vh:", Vh)