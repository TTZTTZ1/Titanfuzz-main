import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5, 5)

# Values to be scattered
values = torch.tensor([1, 2, 3])

# Indices where values will be placed
indices = torch.tensor([[0, 1, 2], [3, 4, 0]])

# Scatter the values into the tensor
result = torch.scatter(tensor, 1, indices, values.unsqueeze(1))

print(result)