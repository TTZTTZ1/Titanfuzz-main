import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])

# Use torch.topk to find the top 2 values and their indices
top_values, top_indices = torch.topk(tensor, k=2)

print("Top values:", top_values)
print("Top indices:", top_indices)