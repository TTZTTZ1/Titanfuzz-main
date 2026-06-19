import torch

# Create a random complex tensor
A = torch.randn(3, 4, dtype=torch.cfloat)

# Compute QR decomposition using 'complete' mode
Q, R = torch.linalg.qr(A, mode='complete')

# Print the results
print("Q:", Q)
print("R:", R)