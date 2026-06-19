import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply Tanh activation
tanh = nn.Tanh()
output_tensor = tanh(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after Tanh Activation:")
print(output_tensor)