import torch

# Create a tensor
a = torch.arange(30).view(6, 5)

# Split the tensor into chunks of size 3 along dimension 1
chunks = torch.split(a, 3, dim=1)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")