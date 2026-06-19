import torch

# Create a tensor
tensor = torch.tensor([[10, 20, 30], [40, 50, 60]])

# Find the indices of the minimum values along dimension 1
indices_of_min = torch.argmin(tensor, dim=1)

print(indices_of_min)