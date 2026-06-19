import torch

# Create a tensor
tensor = torch.randn(10)

# Split the tensor into 5 chunks of size 2
split_tensors = torch.split(tensor, 2)

# Print each split tensor
for i, chunk in enumerate(split_tensors):
    print(f"Chunk {i+1}: {chunk}")