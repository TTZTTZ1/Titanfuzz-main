import torch

# Create a tensor
tensor = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Call torch.sort
sorted_tensor, indices = torch.sort(tensor)

print("Sorted Tensor:", sorted_tensor)
print("Indices:", indices)