import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Use torch.topk to find the top 2 largest elements along the last dimension
top_k_values, top_k_indices = torch.topk(input_tensor, k=2, dim=-1, largest=True, sorted=True)

print("Top K Values:", top_k_values)
print("Top K Indices:", top_k_indices)