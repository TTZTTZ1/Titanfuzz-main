import torch

# Create a random matrix
A = torch.randn(5, 3)

# Compute QR decomposition
Q, R = torch.linalg.qr(A)

# Print the results
print("Q:", Q)
print("R:", R)