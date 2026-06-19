import torch

# Create a random tensor of shape (6, 4)
input_tensor = torch.randn(6, 4)

# Split the tensor into 3 chunks along dimension 0
chunks = torch.chunk(input_tensor, 3, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print()