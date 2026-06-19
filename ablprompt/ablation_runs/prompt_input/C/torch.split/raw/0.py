import torch

# Create a tensor
a = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])

# Split the tensor into two chunks along dimension 0
chunks = torch.split(a, 2, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")