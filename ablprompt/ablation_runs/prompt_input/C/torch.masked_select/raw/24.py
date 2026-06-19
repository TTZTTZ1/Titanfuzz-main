import torch

# Create a random tensor and a boolean mask
input_tensor = torch.randn(4, 5)
mask = torch.rand(4, 5) > 0.5

# Use torch.masked_select to select elements from input_tensor where mask is True
selected_elements = torch.masked_select(input_tensor, mask)

print("Input Tensor:")
print(input_tensor)
print("Mask:")
print(mask)
print("Selected Elements:")
print(selected_elements)