import torch

# Create a list of tensors with different shapes but compatible dimensions for concatenation
tensors = [
    torch.tensor([[1, 2], [3, 4]]),
    torch.tensor([[5, 6], [7, 8]])
]

# Concatenate the tensors along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result)