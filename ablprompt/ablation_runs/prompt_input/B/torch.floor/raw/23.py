import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.rand(5) * 10 - 3  # Random values between -3 and 7

# Apply torch.floor to round down each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after floor:", output_tensor)