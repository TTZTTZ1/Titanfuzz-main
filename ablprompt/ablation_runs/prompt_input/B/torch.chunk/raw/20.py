import torch

# Create a large tensor
large_tensor = torch.randn(10, 3, 4)

# Split the tensor into 5 chunks along the first dimension
chunks = torch.chunk(large_tensor, 5, dim=0)

# Print the shapes of each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} shape: {chunk.shape}")