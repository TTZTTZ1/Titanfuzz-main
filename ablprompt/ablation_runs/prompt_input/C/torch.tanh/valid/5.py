import torch

# Create a random tensor of floats between -5 and 5
input_tensor = torch.rand(3, 3) * 10 - 5

# Compute the hyperbolic tangent of the tensor
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor:")
print(output_tensor)