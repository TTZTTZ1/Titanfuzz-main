import torch

# Create a tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 0]])

# Use torch.argmin to find the indices of the minimum values along dimension 1
result = torch.argmin(tensor, dim=1)

print(result)