import torch

# Create a random matrix
matrix = torch.randn(3, 2)

# Compute QR decomposition
q, r = torch.linalg.qr(matrix)

print("Q:", q)
print("R:", r)