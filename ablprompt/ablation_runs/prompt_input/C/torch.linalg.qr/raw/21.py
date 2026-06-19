import torch

# Create a random complex tensor
A = torch.randn(5, 3, dtype=torch.cfloat)

# Compute the QR decomposition using the 'reduced' mode
Q, R = torch.linalg.qr(A, mode='reduced')

# Verify the result
assert torch.allclose(A, torch.matmul(Q, R)), "The QR decomposition does not match the original matrix"

print("QR decomposition successful!")