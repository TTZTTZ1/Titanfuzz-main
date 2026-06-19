import torch

# Create a tensor
a = torch.randn(10, 3)

# Split the tensor into chunks of size 4 along dimension 0
chunks = torch.split(a, 4, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")