import torch

# Example tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])

# Using torch.topk to get the top 2 elements
top_k_values, top_k_indices = torch.topk(tensor, k=2)

print("Top K Values:", top_k_values)
print("Top K Indices:", top_k_indices)