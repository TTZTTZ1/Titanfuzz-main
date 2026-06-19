import torch

# Create three tensors with different shapes but compatible for concatenation along dimension 1
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6]])
c = torch.tensor([[7, 8], [9, 10]])

# Concatenate tensors along dimension 1
result = torch.cat((a, b, c), dim=1)

print(result)