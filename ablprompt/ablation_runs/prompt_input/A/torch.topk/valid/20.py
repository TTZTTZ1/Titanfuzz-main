import torch

# Example tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Using torch.topk to get the top 3 values and their indices
topk_values, topk_indices = torch.topk(tensor, k=3)

print("Top K Values:", topk_values)
print("Top K Indices:", topk_indices)