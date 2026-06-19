import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Use torch.topk to find the top 2 largest elements along dimension 1
top_k_values, top_k_indices = torch.topk(x, k=2, dim=1)

print("Top K Values:")
print(top_k_values)
print("Top K Indices:")
print(top_k_indices)