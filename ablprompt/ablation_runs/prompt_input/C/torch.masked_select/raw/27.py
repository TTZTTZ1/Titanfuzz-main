import torch

# Create a random tensor and a boolean mask
input_tensor = torch.randn(4, 5)
mask = torch.randint(0, 2, (4, 5)).bool()

# Use torch.masked_select to select elements from the input tensor where the mask is True
selected_elements = torch.masked_select(input_tensor, mask)

print("Input Tensor:\n", input_tensor)
print("Mask:\n", mask)
print("Selected Elements:\n", selected_elements)