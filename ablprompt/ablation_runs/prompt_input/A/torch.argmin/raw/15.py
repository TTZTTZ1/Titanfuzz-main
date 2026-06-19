import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 0]])

# Find the index of the minimum value in the tensor
min_index = torch.argmin(tensor)

print("Index of the minimum value:", min_index)