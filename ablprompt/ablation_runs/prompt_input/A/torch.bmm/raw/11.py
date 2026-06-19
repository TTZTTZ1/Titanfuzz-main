import torch

# Create two 3D tensors for batch matrix multiplication
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)

# Perform batch matrix multiplication using torch.bmm
result = torch.bmm(batch1, batch2)

print(result)