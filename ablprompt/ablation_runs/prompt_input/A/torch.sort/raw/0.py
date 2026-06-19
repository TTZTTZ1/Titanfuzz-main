import torch

# Create a tensor of random numbers
tensor = torch.randn(10)

# Sort the tensor
sorted_tensor, indices = torch.sort(tensor)

print("Original Tensor:", tensor)
print("Sorted Tensor:", sorted_tensor)
print("Indices:", indices)