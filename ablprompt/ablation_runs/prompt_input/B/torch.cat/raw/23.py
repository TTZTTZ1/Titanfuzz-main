import torch

# Create a list of tensors with different shapes but compatible dimensions for concatenation
tensors = [
    torch.randn(2, 3),
    torch.randn(2, 4),
    torch.randn(2, 5)
]

# Concatenate tensors along the second dimension (dim=1)
result = torch.cat(tensors, dim=1)

print(result)