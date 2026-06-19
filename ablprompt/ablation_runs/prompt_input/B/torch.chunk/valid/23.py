import torch

# Create a large tensor
input_tensor = torch.randn(10, 5, 3)

# Split the tensor into 4 chunks along the first dimension
chunks = torch.chunk(input_tensor, 4, dim=0)

# Print the shapes of each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} shape: {chunk.shape}")