import torch

# Create a large tensor
large_tensor = torch.randn(100, 32)

# Split the tensor into chunks of size 16 along dimension 1
chunks = torch.split(large_tensor, 16, dim=1)

# Print the shapes of each chunk to verify the split
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} shape: {chunk.shape}")