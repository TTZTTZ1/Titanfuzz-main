import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(3, 3, requires_grad=True)

# Compute the tangent of each element in the input tensor
output_tensor = torch.tan(input_tensor)

# Print the input and output tensors
print("Input Tensor:")
print(input_tensor)
print("Output Tensor:")
print(output_tensor)

# Perform a backward pass to compute gradients
output_tensor.sum().backward()

# Print the gradients of the input tensor
print("Gradients of Input Tensor:")
print(input_tensor.grad)