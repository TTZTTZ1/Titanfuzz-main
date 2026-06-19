import torch

# Create a random tensor of shape (5, 3)
input_tensor = torch.randn(5, 3)

# Split the tensor into 2 chunks along dimension 0
chunks = torch.chunk(input_tensor, chunks=2, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")