import torch

# Create a sample tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Call torch.topk to get the top 2 values and their indices along dimension 1
top_values, top_indices = torch.topk(tensor, k=2, dim=1)

print("Top Values:", top_values)
print("Top Indices:", top_indices)