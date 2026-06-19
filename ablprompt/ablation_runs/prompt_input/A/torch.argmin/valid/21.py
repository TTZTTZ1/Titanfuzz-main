import torch

# Create a tensor
tensor = torch.tensor([[10, 50, 30], [60, 20, 40]])

# Find the indices of the minimum values along dimension 1
indices_of_min = torch.argmin(tensor, dim=1)

print(indices_of_min)