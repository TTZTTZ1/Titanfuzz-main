import torch

# Create a tensor where we want to scatter values
tensor = torch.zeros(5)

# Define the indices and the source tensor from which to scatter values
indices = torch.tensor([0, 2, 4])
source = torch.tensor([1.0, 2.0, 3.0])

# Use torch.scatter to update the tensor at specified indices with values from the source tensor
tensor.scatter_(dim=0, index=indices, src=source)

print(tensor)