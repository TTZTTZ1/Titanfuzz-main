import torch

# Create a random tensor with values in the range [-10, 10]
input_tensor = torch.randn(5, 5) * 20

# Compute the hyperbolic tangent of the input tensor
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nOutput Tensor:")
print(output_tensor)