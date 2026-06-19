import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.rand(5) * 10  # Random values between 0 and 10

# Apply torch.floor to the tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)