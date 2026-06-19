import torch

# Create a tensor to split
tensor = torch.randn(10, 3)

# Split the tensor into chunks of size 2 along dimension 0
chunks = torch.split(tensor, 2, dim=0)

# Print each chunk
for chunk in chunks:
    print(chunk)