import torch

# Create a random complex tensor
A = torch.randn(5, 3, dtype=torch.cfloat)

# Compute QR decomposition
Q, R = torch.linalg.qr(A, mode='reduced')

print("Q:", Q)
print("R:", R)