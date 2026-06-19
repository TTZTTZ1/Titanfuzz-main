import torch

# Create a random tensor
tensor = torch.randn(10, 5)

# Use torch.topk to find the top 3 values and their indices
values, indices = torch.topk(tensor, k=3)

print("Values:", values)
print("Indices:", indices)