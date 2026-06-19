import torch

# Create some example tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Concatenate tensors along dimension 0
result = torch.cat((a, b), dim=0)

print(result)