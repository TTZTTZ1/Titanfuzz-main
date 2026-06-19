import torch

# Create a tensor
tensor = torch.randn(10, 5)

# Use torch.topk to get the top 3 elements along dimension 1
values, indices = torch.topk(tensor, k=3, dim=1)

print("Values:", values)
print("Indices:", indices)