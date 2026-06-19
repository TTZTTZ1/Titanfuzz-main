import torch

# Create a tensor
a = torch.randn(8, 3)

# Split the tensor into 4 chunks along dimension 0
chunks = torch.split(a, 2, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")