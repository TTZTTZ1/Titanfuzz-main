import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.5, 2.3, 4.7, -1.2])

# Apply torch.floor to round down each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after floor:", output_tensor)