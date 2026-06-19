import torch

# Create a random tensor
input_tensor = torch.randn(10, 3)

# Split the tensor into 4 chunks along the first dimension (dim=0)
chunks = torch.chunk(input_tensor, 4, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")