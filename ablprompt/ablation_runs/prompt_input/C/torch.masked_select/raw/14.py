import torch

# Create a random tensor of size 4x3
input_tensor = torch.randn(4, 3)

# Create a boolean mask of the same shape as input_tensor
mask = input_tensor > 0

# Use torch.masked_select to select elements from input_tensor where the corresponding element in mask is True
selected_elements = torch.masked_select(input_tensor, mask)

print("Input Tensor:")
print(input_tensor)
print("\nMask:")
print(mask)
print("\nSelected Elements:")
print(selected_elements)