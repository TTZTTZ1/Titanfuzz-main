import torch

# Create a random tensor
tensor = torch.randn(10, 5)

# Use torch.topk to find the top 3 values and their indices
top_values, top_indices = torch.topk(tensor, k=3)

print("Top Values:", top_values)
print("Top Indices:", top_indices)