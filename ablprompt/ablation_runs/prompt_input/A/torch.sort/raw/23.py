import torch

# Create a tensor
tensor = torch.tensor([3, 1, 2])

# Sort the tensor
sorted_tensor, indices = torch.sort(tensor)

print("Sorted Tensor:", sorted_tensor)
print("Indices:", indices)