import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 4)

# Define indices and source tensor
indices = torch.tensor([[0, 1], [2, 0]])
source = torch.tensor([[1, 1], [1, 1]])

# Use torch.scatter to update the tensor
result = torch.scatter(tensor, 0, indices, source)

print(result)