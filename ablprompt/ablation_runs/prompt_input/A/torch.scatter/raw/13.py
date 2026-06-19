import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5, 5)

# Values to be scattered
values = torch.tensor([10, 20, 30])

# Indices where values will be placed
indices = torch.tensor([[0, 4], [2, 1]])

# Perform the scatter operation
tensor.scatter_(1, indices, values.unsqueeze(-1))

print(tensor)