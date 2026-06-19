import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Use torch.argmax to find the indices of the maximum values along dimension 1
indices_of_max = torch.argmax(tensor, dim=1)

print(indices_of_max)