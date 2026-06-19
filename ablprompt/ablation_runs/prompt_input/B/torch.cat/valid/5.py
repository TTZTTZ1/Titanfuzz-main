import torch

# Create a list of tensors with different shapes but compatible for concatenation along dimension 1
tensors = [
    torch.randn(2, 3),
    torch.randn(2, 4),
    torch.randn(2, 5)
]

# Concatenate the tensors along dimension 1
result = torch.cat(tensors, dim=1)

print(result)