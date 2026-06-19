import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Use torch.unsqueeze to add a new dimension at index 0
unsqueezed_tensor = torch.unsqueeze(tensor, 0)

print(unsqueezed_tensor)