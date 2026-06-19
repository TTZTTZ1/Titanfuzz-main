import torch

# Create a random tensor with float values between -10 and 10
input_tensor = torch.rand(5) * 20 - 10

# Apply torch.ceil to round up each element
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)