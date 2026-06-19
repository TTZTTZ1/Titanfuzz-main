import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute the QR decomposition
Q, R = torch.linalg.qr(A, mode='reduced')

print("Q:", Q)
print("R:", R)