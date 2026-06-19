import torch

# Create some sample tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
c = torch.tensor([[9, 10], [11, 12]])

# Concatenate tensors along dimension 0
result = torch.cat((a, b, c), dim=0)

print(result)