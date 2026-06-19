import torch

# Create a random tensor of floats between -10 and 10
input_tensor = torch.randn(5, 5) * 20

# Compute the hyperbolic tangent of the input tensor
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor after tanh:\n", output_tensor)