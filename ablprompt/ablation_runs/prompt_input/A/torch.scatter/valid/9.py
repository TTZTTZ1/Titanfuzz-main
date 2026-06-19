import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5)

# Define indices and source values for scattering
indices = torch.tensor([0, 2, 4])
values = torch.tensor([1.0, 2.0, 3.0])

# Perform the scatter operation
result = torch.scatter(tensor, 0, indices, values)

print(result)