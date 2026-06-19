import torch

# Create a tensor
a = torch.arange(24).reshape(3, 4)

# Split the tensor into chunks of size 2 along dimension 1
chunks = torch.split(a, 2, dim=1)

# Print the chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")