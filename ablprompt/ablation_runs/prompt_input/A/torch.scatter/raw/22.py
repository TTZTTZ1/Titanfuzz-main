import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 3)

# Define indices and source tensors
indices = torch.tensor([[0, 1], [2, 0]])
source = torch.tensor([[9, 8], [7, 6]])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, source)

print(result)