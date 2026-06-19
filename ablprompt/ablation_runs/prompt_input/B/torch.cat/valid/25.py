import torch

# Create a list of tensors with different shapes but the same number of elements in the concatenation dimension
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(5, 3)
]

# Concatenate the tensors along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result.shape)  # Expected output: torch.Size([11, 3])