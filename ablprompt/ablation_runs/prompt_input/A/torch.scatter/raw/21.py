import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5, 5)

# Define indices and source values for scattering
indices = torch.tensor([[0, 2], [1, 3]])
values = torch.tensor([9, 8])

# Perform the scatter operation
tensor.scatter_(0, indices, values)

print(tensor)