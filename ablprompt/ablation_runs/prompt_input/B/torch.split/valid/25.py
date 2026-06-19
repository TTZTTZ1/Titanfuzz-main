import torch

# Create a tensor
a = torch.randn(10, 3, 4)

# Split the tensor into chunks of size 3 along dimension 1
chunks = torch.split(a, 3, dim=1)

# Print the chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}:")
    print(chunk)