import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5, 6])

# Split the tensor into chunks of size 2
chunks = torch.chunk(tensor, 2)

# Print each chunk
for chunk in chunks:
    print(chunk)