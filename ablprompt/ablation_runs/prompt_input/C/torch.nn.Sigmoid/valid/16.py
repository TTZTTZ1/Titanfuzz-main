import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 5)

# Apply Sigmoid activation
sigmoid = nn.Sigmoid()
output_tensor = sigmoid(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)