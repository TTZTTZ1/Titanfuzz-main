import torch

# Create a tensor to scatter values into
tensor = torch.zeros(4, 4)

# Define indices and source values for scattering
indices = torch.tensor([[0, 1], [2, 3]])
values = torch.tensor([[1, 2], [3, 4]])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, values)

print(result)