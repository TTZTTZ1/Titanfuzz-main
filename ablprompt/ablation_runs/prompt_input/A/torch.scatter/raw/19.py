import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 4)

# Define indices and updates for scattering
indices = torch.tensor([[0, 1], [2, 0]])
updates = torch.tensor([[1, 2], [3, 4]])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, updates)

print(result)