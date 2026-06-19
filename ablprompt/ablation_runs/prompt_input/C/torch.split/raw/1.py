import torch

# Create a random tensor
tensor = torch.randn(8, 3)

# Split the tensor into 3 chunks along dimension 0
chunks = torch.split(tensor, [2, 3, 3], dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")