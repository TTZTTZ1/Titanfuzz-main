import torch

# Create a tensor where we will scatter values into
tensor = torch.zeros(5, 5)

# Define the indices and source values for scattering
indices = torch.tensor([[0, 1], [2, 3]])
values = torch.tensor([99, 88])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, values)

print(result)