import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply ReLU activation
relu_layer = nn.ReLU(inplace=False)
output_tensor = relu_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ReLU:", output_tensor)