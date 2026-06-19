import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5])

# Call torch.topk
values, indices = torch.topk(tensor, k=3)

print("Values:", values)
print("Indices:", indices)