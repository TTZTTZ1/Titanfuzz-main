import torch

# Example of using torch.einsum for batch matrix multiplication
batch_size = 5
dim1 = 3
dim2 = 4
dim3 = 6

# Create random tensors
a = torch.randn(batch_size, dim1, dim2)
b = torch.randn(batch_size, dim2, dim3)

# Perform batch matrix multiplication using einsum
result = torch.einsum('bij,bjk->blk', a, b)

print(result.shape)  # Should print: torch.Size([5, 3, 6])