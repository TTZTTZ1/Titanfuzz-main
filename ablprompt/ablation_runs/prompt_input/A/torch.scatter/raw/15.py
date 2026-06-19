import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 4)

# Define the indices where the values will be scattered
indices = torch.tensor([[0, 2], [1, 3]])

# Define the source tensor containing the values to scatter
source = torch.tensor([[9, 8], [7, 6]])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, source)

print(result)