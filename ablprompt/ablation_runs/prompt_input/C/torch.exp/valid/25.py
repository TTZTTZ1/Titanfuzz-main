import torch

# Create a random tensor of floats
input_tensor = torch.randn(5, 5, requires_grad=True)

# Compute the exponential of the input tensor
output_tensor = torch.exp(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)