import torch

# Create a tensor
tensor = torch.tensor([[10, 20, 30], [40, 50, 60]])

# Use torch.argmin to find the index of the minimum value in the tensor
min_index = torch.argmin(tensor)

print("Index of the minimum value:", min_index)