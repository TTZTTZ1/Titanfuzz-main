import torch

# Create a list of tensors with varying dimensions but the same shape excluding the concatenation dimension
tensors = [
    torch.randn(2, 3),
    torch.randn(2, 3),
    torch.randn(2, 3)
]

# Concatenate the tensors along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result)