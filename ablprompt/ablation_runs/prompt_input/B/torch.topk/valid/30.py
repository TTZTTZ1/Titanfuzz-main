import torch

# Create a random tensor
x = torch.randn(3, 4)

# Use torch.topk to find the top 2 largest elements along dimension 1
top_values, top_indices = torch.topk(x, k=2, dim=1)

print("Top Values:", top_values)
print("Top Indices:", top_indices)