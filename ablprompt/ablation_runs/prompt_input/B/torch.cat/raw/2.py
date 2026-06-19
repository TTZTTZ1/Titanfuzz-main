import torch

# Create a list of tensors with different shapes but matching dimensions except for the first
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(6, 3)
]

# Concatenate along the second dimension (dim=1)
result = torch.cat(tensors, dim=1)

print(result)