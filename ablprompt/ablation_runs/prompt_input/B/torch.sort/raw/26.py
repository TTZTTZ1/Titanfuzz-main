import torch

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Sort the tensor along the second dimension in descending order and get stable results
sorted_tensor, indices = torch.sort(input_tensor, dim=1, descending=True, stable=True)

print("Sorted Tensor:")
print(sorted_tensor)
print("Indices:")
print(indices)