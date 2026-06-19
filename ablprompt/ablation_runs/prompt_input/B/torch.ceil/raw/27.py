import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-1.5, -0.2, 0.7, 2.3])

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ceil:", output_tensor)