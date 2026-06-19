import torch

# Create a list of tensors with varying dimensions but matching shapes except in the concatenation dimension
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(6, 3)
]

# Concatenate along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result)