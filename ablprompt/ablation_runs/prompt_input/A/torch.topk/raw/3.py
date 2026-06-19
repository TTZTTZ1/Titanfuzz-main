import torch

# Create a tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Use torch.topk to get the top 2 values and their indices
values, indices = torch.topk(tensor, k=2)

print("Values:", values)
print("Indices:", indices)