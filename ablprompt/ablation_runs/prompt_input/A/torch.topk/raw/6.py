import torch

# Create a random tensor
tensor = torch.randn(10)

# Call torch.topk to find the top 3 values and their indices
topk_values, topk_indices = torch.topk(tensor, k=3)

print("Top K Values:", topk_values)
print("Top K Indices:", topk_indices)