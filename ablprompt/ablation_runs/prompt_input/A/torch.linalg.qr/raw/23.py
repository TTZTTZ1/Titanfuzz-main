import torch

# Create a random matrix
A = torch.randn(3, 4)

# Compute QR decomposition
Q, R = torch.linalg.qr(A)

print("Q:", Q)
print("R:", R)