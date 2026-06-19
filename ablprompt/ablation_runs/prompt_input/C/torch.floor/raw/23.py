import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.7, -2.5, 4.0])

# Apply torch.floor to get the floor values
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying torch.floor:", output_tensor)