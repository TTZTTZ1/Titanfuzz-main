import torch

a = torch.randn(10, 3, 4)
split_sizes = [2, 3, 5]
chunks = torch.split(a, split_sizes, dim=0)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk.shape}")