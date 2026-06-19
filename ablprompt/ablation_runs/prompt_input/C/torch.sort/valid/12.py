import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Sort the tensor along the second dimension in descending order
sorted_tensor, indices = torch.sort(input_tensor, dim=1, descending=True)

print("Sorted Tensor:")
print(sorted_tensor)
print("Indices:")
print(indices)