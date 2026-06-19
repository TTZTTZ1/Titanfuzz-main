import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5])

# Use torch.chunk to split the tensor into chunks of size 2
chunks = torch.chunk(tensor, 2)

# Print the result
print(chunks)