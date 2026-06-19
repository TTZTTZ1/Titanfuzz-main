import torch

# Create a random tensor
x = torch.randn(3, 4)

# Find the top 2 largest values and their indices along the last dimension
top_values, top_indices = torch.topk(x, k=2)

print("Top Values:", top_values)
print("Top Indices:", top_indices)