import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute QR decomposition using the 'complete' mode
Q, R = torch.linalg.qr(A, mode='complete')

print("Q:", Q)
print("R:", R)