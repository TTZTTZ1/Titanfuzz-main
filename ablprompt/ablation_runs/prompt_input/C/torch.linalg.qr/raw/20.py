import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute the QR decomposition using the 'complete' mode
Q, R = torch.linalg.qr(A, mode='complete')

# Verify the result
assert torch.allclose(A, torch.matmul(Q, R))

print("Q:", Q)
print("R:", R)