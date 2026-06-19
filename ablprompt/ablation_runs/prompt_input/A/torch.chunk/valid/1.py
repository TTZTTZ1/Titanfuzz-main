import torch

# Create a tensor
tensor = torch.randn(10)

# Use torch.chunk to split the tensor into 5 chunks
chunks = torch.chunk(tensor, 5)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")