import torch

# Create a random tensor of shape (8, 3)
a = torch.randn(8, 3)

# Split the tensor into chunks of size 2 along dimension 0
chunks = torch.split(a, 2)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")