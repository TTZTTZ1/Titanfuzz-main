import torch

# Create a list of tensors with varying shapes but the same number of dimensions
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(6, 3)
]

# Concatenate along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result.shape)  # Expected output: torch.Size([12, 3])