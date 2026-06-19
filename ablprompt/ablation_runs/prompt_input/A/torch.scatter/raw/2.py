import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5)

# Values to be scattered
values = torch.tensor([10, 20])

# Indices where values will be placed
indices = torch.tensor([0, 4])

# Perform the scatter operation
result = torch.scatter(tensor, 0, indices, values)

print(result)