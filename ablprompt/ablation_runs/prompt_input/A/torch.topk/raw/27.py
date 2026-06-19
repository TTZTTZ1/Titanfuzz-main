import torch

# Create a tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Use torch.topk to get the top 2 values and their indices
top_values, top_indices = torch.topk(tensor, k=2)

print("Top Values:", top_values)
print("Top Indices:", top_indices)