import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.rand(5) * 10 - 5  # Random values between -5 and 5

# Apply torch.floor to the tensor
result_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after applying torch.floor:", result_tensor)