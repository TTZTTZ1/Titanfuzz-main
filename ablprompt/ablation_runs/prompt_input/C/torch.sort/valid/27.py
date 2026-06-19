import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Sort the tensor along dimension 1 in descending order
sorted_tensor, indices = torch.sort(input_tensor, dim=1, descending=True)

print("Sorted Tensor:\n", sorted_tensor)
print("Indices:\n", indices)