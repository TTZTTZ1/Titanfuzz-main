import torch

# Create a random complex tensor
A = torch.randn(5, 3, dtype=torch.cfloat)

# Compute QR decomposition in complete mode
Q, R = torch.linalg.qr(A, mode='complete')

# Verify the result
assert torch.allclose(A, Q @ R), "The original matrix does not match the reconstructed matrix."
print("QR decomposition successful.")