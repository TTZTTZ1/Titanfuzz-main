import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply Sigmoid activation
sigmoid_layer = nn.Sigmoid()
output_tensor = sigmoid_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Sigmoid:", output_tensor)