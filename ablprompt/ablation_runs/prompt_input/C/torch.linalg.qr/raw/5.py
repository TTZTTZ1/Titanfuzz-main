import torch

# Create a random complex tensor
A = torch.randn(5, 3, dtype=torch.cfloat)

# Compute QR decomposition
Q, R = torch.linalg.qr(A, mode='reduced')

# Verify the result
assert torch.allclose(A, torch.matmul(Q, R)), "The QR decomposition does not satisfy A ≈ Q @ R"

print("QR decomposition successful!")