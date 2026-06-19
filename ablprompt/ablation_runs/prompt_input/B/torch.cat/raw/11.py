import torch

# Create a list of tensors with different shapes but compatible for concatenation
tensors = [
    torch.randn(2, 3),
    torch.randn(2, 4),
    torch.randn(2, 5)
]

# Concatenate along the second dimension (columns)
result = torch.cat(tensors, dim=1)

print(result)