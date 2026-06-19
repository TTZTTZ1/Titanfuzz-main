import torch

# Create a random tensor
input_tensor = torch.randn(10, 3, 4)

# Split the tensor into 3 chunks along the first dimension
chunks = torch.chunk(input_tensor, 3, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")