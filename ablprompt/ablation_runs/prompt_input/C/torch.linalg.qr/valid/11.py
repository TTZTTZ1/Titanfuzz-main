import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute QR decomposition using the 'reduced' mode
Q, R = torch.linalg.qr(A, mode='reduced')

# Verify the result
assert torch.allclose(A, Q @ R), "The original matrix does not match Q @ R"

print("Q:", Q)
print("R:", R)