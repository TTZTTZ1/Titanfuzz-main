import torch

# Create a tensor
a = torch.randn(10, 5)

# Split the tensor into chunks of size 3 along dimension 0
chunks = torch.split(a, 3, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")