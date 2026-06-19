import torch

# Create a large tensor
large_tensor = torch.randn(100, 50)

# Split the tensor into 4 chunks along the first dimension
chunks = torch.chunk(large_tensor, 4, dim=0)

# Print the shapes of the chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} shape: {chunk.shape}")