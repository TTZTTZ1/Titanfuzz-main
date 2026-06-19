import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 3)

# Apply the tanh function to the input tensor
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after applying tanh:")
print(output_tensor)