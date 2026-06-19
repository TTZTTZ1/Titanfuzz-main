import torch

# Create a random matrix
A = torch.randn(5, 3)

# Compute QR decomposition
Q, R = torch.linalg.qr(A)

print("Matrix A:")
print(A)
print("\nOrthogonal Matrix Q:")
print(Q)
print("\nUpper Triangular Matrix R:")
print(R)