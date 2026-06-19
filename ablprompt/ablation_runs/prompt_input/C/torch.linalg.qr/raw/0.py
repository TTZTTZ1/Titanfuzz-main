import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cdouble)

# Compute QR decomposition
Q, R = torch.linalg.qr(A, mode='reduced')

# Verify the result
assert torch.allclose(A, Q @ R), "The original matrix does not match Q @ R"

print("QR decomposition successful:")
print("Q:", Q)
print("R:", R)