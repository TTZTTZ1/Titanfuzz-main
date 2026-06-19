import torch

# Create a sample matrix
matrix = torch.tensor([[12., -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=torch.float32)

# Call the torch.linalg.qr function
q, r = torch.linalg.qr(matrix)

print("Q:", q)
print("R:", r)