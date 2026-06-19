import torch

# Create a random tensor with negative and positive values
input_tensor = torch.randn(5) * 10  # Random values between -10 and 10

# Compute the square root of the tensor
result = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Square Root Result:", result)