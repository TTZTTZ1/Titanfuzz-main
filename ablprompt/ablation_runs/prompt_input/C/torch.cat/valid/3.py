import torch

# Create a list of tensors with varying dimensions but matching shapes in all dimensions except the first
tensors = [
    torch.randn(1, 3),
    torch.randn(2, 3),
    torch.randn(3, 3)
]

# Concatenate the tensors along the first dimension (dim=0)
result = torch.cat(tensors, dim=0)

print(result)