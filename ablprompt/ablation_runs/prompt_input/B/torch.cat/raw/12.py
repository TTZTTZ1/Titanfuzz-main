import torch

# Create a list of tensors with different shapes but matching dimensions except for the concatenation dimension
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(6, 3)
]

# Concatenate along the first dimension (dim=0)
result = torch.cat(tensors, dim=0)

print(result)