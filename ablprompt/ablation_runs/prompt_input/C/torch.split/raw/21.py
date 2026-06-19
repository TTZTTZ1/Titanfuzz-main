import torch

# Create a tensor
a = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])

# Split the tensor into chunks of size 2 along dimension 0
result = torch.split(a, 2)

print(result)