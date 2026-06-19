import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Call torch.topk
values, indices = torch.topk(tensor, k=3)

print("Values:", values)
print("Indices:", indices)