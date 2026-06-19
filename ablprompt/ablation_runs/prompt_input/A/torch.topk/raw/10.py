import torch

# Example tensor
tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Using torch.topk to get the top 2 values and their indices
values, indices = torch.topk(tensor, k=2)

print("Values:", values)
print("Indices:", indices)