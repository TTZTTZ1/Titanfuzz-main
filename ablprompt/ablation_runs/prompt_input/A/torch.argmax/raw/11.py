import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3])

# Use torch.argmax to find the index of the maximum value
max_index = torch.argmax(tensor)

print("The index of the maximum value is:", max_index)