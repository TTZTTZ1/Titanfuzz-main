import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Use torch.topk to find the top 2 largest values and their indices along the second dimension
top_k_values, top_k_indices = torch.topk(input_tensor, k=2, dim=1, largest=True, sorted=True)

print("Top K Values:")
print(top_k_values)
print("Top K Indices:")
print(top_k_indices)