import torch

# Create a list of tensors with different shapes but the same number of dimensions except for the first dimension
tensors = [
    torch.randn(2, 3),
    torch.randn(4, 3),
    torch.randn(6, 3)
]

# Concatenate the tensors along the second dimension (dim=1)
result = torch.cat(tensors, dim=1)

print(result)