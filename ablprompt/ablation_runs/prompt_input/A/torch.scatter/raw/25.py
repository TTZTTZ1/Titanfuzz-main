import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 4)

# Define the indices where the values will be scattered
indices = torch.tensor([[0, 2], [1, 3]])

# Define the source tensor containing the values to scatter
values = torch.tensor([[9, 8], [7, 6]])

# Use torch.scatter to update the tensor
result = torch.scatter(tensor, 1, indices, values)

print(result)