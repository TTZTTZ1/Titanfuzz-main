import torch

# Create a large tensor
input_tensor = torch.randn(10, 3, 4)

# Split the tensor into 5 chunks along the first dimension (dim=0)
chunks = torch.chunk(input_tensor, 5, dim=0)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")