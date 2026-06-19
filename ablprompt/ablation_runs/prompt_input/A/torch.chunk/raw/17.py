import torch

# Create a tensor
tensor = torch.randn(10)

# Split the tensor into 2 chunks
chunks = torch.chunk(tensor, 2)

# Print each chunk
for chunk in chunks:
    print(chunk)