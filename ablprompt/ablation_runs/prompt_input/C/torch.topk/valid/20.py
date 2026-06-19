import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Use torch.topk to find the top 2 largest elements along dimension 1
topk_values, topk_indices = torch.topk(input_tensor, k=2, dim=1)

print("TopK Values:", topk_values)
print("TopK Indices:", topk_indices)