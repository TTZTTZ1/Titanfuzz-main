import torch

# Create a list of tensors with different shapes but matching dimensions except for the first one
tensors = [
    torch.tensor([[1, 2], [3, 4]]),
    torch.tensor([[5, 6], [7, 8]]),
    torch.tensor([[9, 10], [11, 12]])
]

# Concatenate the tensors along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result)