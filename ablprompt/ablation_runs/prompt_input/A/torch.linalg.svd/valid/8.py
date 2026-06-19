import torch

# Create a sample tensor
A = torch.tensor([[1., 2.], [3., 4.]])

# Call the SVD function from torch.linalg
U, S, Vh = torch.linalg.svd(A)

print("U:", U)
print("S:", S)
print("Vh:", Vh)