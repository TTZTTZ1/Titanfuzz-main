import torch

# Create a tensor
tensor = torch.tensor([[10, 20], [30, 40]])

# Find the index of the minimum value
min_index = torch.argmin(tensor)

print("The index of the minimum value is:", min_index)