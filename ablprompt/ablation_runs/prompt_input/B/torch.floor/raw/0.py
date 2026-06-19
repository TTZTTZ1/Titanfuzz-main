import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.7, -0.5, -2.8], dtype=torch.float32)

# Apply torch.floor to get the largest integer less than or equal to each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)