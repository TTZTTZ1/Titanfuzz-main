import torch

# Create a list of tensors with different shapes but the same number of elements in the concatenation dimension
tensors = [
    torch.randn(3),
    torch.randn(4),
    torch.randn(5)
]

# Concatenate the tensors along the first dimension
result = torch.cat(tensors, dim=0)

print(result)