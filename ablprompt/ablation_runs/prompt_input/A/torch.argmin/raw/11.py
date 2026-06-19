import torch

# Create a tensor
tensor = torch.tensor([[10, 50, 30], [60, 20, 40]])

# Use torch.argmin to find the indices of the minimum values along axis 1
result = torch.argmin(tensor, dim=1)

print(result)