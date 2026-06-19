import torch

# Create a tensor
tensor = torch.tensor([[10, 2], [3, 4]])

# Use torch.argmin to find the indices of the minimum values along dim=1
result = torch.argmin(tensor, dim=1)

print(result)