import torch

# Create a random tensor
input_tensor = torch.randn(4, 3)

# Sort the tensor along the first dimension in descending order
sorted_tensor, indices = torch.sort(input_tensor, dim=0, descending=True, stable=True)

print("Sorted Tensor:")
print(sorted_tensor)
print("Indices:")
print(indices)