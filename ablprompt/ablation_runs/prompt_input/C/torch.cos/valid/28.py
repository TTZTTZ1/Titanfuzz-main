import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(5, requires_grad=True)

# Compute the cosine of the input tensor
output_tensor = torch.cos(input_tensor)

# Print the results
print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)