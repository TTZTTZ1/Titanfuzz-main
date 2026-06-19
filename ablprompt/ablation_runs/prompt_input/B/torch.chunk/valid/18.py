import torch

# Create a large tensor
large_tensor = torch.randn(10, 3, 5)

# Split the tensor into 4 chunks along the first dimension
chunks = torch.chunk(large_tensor, 4, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")