import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-1.2, 3.5, -4.8, 0.0], dtype=torch.float)

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying torch.ceil:", output_tensor)