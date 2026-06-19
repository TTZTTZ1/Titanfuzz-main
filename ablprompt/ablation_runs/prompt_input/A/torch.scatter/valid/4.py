import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5)

# Define the indices and the source values
indices = torch.tensor([0, 2, 4])
values = torch.tensor([1.0, 2.0, 3.0])

# Use torch.scatter to update the tensor
result = torch.scatter(tensor, 0, indices, values)

print(result)