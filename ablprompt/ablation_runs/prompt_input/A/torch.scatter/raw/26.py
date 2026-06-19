import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 4)

# Define indices and source tensors
indices = torch.tensor([[0, 2], [1, 3]])
source = torch.tensor([[1, 1], [2, 2]])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, source)

print(result)