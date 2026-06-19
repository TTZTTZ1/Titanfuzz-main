import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 3)

# Define indices and source values for scattering
indices = torch.tensor([[0, 2], [1, 1]])
values = torch.tensor([5, 7])

# Perform the scatter operation
tensor.scatter_(0, indices, values)

print(tensor)