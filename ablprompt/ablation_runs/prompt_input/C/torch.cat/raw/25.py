import torch

# Create a list of tensors with different shapes but compatible dimensions for concatenation
tensors = [
    torch.randn(3, 4),
    torch.randn(3, 4),
    torch.randn(3, 4)
]

# Concatenate the tensors along dimension 1
result = torch.cat(tensors, dim=1)

print(result.shape)  # Expected output: torch.Size([3, 12])