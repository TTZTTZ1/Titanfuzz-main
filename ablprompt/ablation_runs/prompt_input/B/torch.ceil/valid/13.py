import torch

# Create a random tensor of floats
input_tensor = torch.rand(3, 4) * 10 - 5  # Values between -5 and 5

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after applying torch.ceil:")
print(output_tensor)