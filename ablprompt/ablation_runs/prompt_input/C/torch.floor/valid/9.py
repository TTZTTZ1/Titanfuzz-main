import torch

# Create a random tensor with floating-point values
input_tensor = torch.rand(5) * 10 - 3  # Values between -3 and 7

# Apply torch.floor to the tensor
result_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after applying torch.floor:", result_tensor)