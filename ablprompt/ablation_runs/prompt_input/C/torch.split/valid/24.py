import torch

# Create a tensor
a = torch.randn(10, 3)

# Split the tensor into chunks of size 2 along dimension 0
chunks = torch.split(a, 2, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print()