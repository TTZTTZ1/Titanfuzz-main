import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Use torch.topk to find the top 3 values and their indices
top_k_values, top_k_indices = torch.topk(tensor, k=3)

print("Top K Values:", top_k_values)
print("Top K Indices:", top_k_indices)