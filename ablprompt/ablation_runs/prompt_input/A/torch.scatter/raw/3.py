import torch

# Create a tensor to scatter values into
tensor = torch.zeros(3, 4)

# Define indices and source values
indices = torch.tensor([[0, 1], [2, 0]])
values = torch.tensor([9, 8])

# Perform the scatter operation
result = torch.scatter(tensor, 1, indices, values)

print(result)