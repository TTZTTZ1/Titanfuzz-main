import torch

# Create a random complex tensor
A = torch.randn(5, 3, dtype=torch.cfloat)

# Compute QR decomposition using 'complete' mode
Q, R = torch.linalg.qr(A, mode='complete')

# Verify the result
assert torch.allclose(A, torch.matmul(Q, R)), "The QR decomposition does not match the original matrix."

print("QR decomposition successful:", Q.shape, R.shape)