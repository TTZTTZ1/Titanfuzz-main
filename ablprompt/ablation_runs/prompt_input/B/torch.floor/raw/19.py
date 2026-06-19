import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.rand(4, 4) * 10 - 5  # Random values between -5 and 5

# Apply floor operation
output_tensor = torch.floor(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after applying torch.floor:")
print(output_tensor)