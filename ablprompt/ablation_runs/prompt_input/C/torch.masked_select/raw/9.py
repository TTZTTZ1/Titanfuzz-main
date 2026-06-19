import torch

# Create a random tensor
input_tensor = torch.randn(4, 5)

# Create a boolean mask
mask = (input_tensor > 0).byte()

# Use torch.masked_select to select elements from the input tensor based on the mask
selected_elements = torch.masked_select(input_tensor, mask)

print("Input Tensor:", input_tensor)
print("Mask:", mask)
print("Selected Elements:", selected_elements)