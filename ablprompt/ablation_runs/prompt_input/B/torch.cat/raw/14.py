import torch

# Create a list of tensors with varying shapes but matching dimensions except for the first one
tensors = [
    torch.randn(1, 2),
    torch.randn(2, 2),
    torch.randn(3, 2)
]

# Concatenate tensors along the second dimension (dim=1)
result = torch.cat(tensors, dim=1)

print(result)