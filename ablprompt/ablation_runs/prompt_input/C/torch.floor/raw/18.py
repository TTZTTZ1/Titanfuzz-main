import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.3, 4.7, -1.2, 0.8])

# Apply torch.floor to round down each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)