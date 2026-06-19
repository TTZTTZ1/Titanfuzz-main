import torch

# Create a random complex matrix
A = torch.randn(4, 3, dtype=torch.cfloat)

# Compute QR decomposition using the 'reduced' mode
Q, R = torch.linalg.qr(A, mode='reduced')

print("Q:", Q)
print("R:", R)