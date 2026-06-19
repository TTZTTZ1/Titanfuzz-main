import torch

# Create a random tensor with float values
input_tensor = torch.tensor([1.2, -2.7, 3.5, -4.8], dtype=torch.float)

# Use torch.ceil to round up the elements
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)