import torch

# Create a tensor of zeros
tensor = torch.zeros(3, 4)

# Define indices and updates
indices = torch.tensor([[0, 1], [2, 0]])
updates = torch.tensor([[9, 8], [7, 6]])

# Use torch.scatter to update the tensor
result = torch.scatter(tensor, 0, indices, updates)

print(result)