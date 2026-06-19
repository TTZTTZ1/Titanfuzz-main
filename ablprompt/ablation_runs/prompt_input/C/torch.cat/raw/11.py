import torch

# Create a list of tensors with different shapes but compatible dimensions for concatenation
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(6, 3)
]

# Concatenate tensors along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result)