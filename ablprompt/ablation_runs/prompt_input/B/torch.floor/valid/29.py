import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.5, 2.3, 4.8, -1.2, -3.7])

# Apply torch.floor to the tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)