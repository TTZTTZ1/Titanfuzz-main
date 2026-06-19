import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-2.5, -1.3, 0.7, 1.9, 3])

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)