import torch

# Create a random tensor
tensor = torch.randn(10)

# Use torch.topk to get the top 3 values and their indices
top_values, top_indices = torch.topk(tensor, k=3)

print("Top values:", top_values)
print("Top indices:", top_indices)