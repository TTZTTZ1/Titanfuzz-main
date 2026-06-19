import torch

# Create a sample matrix
A = torch.tensor([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=torch.float32)

# Compute QR decomposition
Q, R = torch.linalg.qr(A)

print("Q:", Q)
print("R:", R)