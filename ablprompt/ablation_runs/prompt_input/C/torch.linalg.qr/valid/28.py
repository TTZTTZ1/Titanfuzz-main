import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute the QR decomposition
Q, R = torch.linalg.qr(A, mode='reduced')

# Verify the result
assert torch.allclose(A, Q @ R), "The QR decomposition does not satisfy A ≈ Q @ R"

print("QR decomposition successful!")