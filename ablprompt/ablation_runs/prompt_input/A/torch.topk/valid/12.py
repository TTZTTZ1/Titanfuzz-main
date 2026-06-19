import torch

# Create a tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Call torch.topk
values, indices = torch.topk(tensor, k=2)

print("Values:", values)
print("Indices:", indices)