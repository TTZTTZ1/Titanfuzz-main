import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Apply torch.floor to get the floor values
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)