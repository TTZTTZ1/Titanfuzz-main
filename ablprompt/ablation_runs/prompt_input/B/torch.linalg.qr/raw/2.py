import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute QR decomposition in complete mode
Q, R = torch.linalg.qr(A, mode='complete')

# Verify the result
assert torch.allclose(A, Q @ R), "The original matrix does not match the QR product"

print("QR decomposition successful:")
print("Q:", Q)
print("R:", R)