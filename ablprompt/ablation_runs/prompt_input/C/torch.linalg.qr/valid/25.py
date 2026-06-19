import torch

# Create a random matrix
A = torch.randn(5, 3, dtype=torch.double)

# Compute the QR decomposition
Q, R = torch.linalg.qr(A, mode='reduced')

# Verify the result
assert torch.allclose(A, Q @ R), "The QR decomposition does not match the original matrix"

print("QR decomposition successful:")
print("Q:", Q)
print("R:", R)