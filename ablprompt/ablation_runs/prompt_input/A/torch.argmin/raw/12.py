import torch

# Create a tensor
tensor = torch.tensor([[10, 20], [30, 40]])

# Use torch.argmin to find the indices of the minimum values along the specified dimension
indices_of_min = torch.argmin(tensor, dim=1)

print(indices_of_min)