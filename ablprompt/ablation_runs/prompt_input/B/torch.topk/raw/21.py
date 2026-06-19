import torch

# Create a random tensor
x = torch.randn(5, 3)

# Use torch.topk to find the top 2 largest elements along dimension 1
top_values, top_indices = torch.topk(x, k=2, dim=1, largest=True, sorted=True)

print("Top Values:", top_values)
print("Top Indices:", top_indices)