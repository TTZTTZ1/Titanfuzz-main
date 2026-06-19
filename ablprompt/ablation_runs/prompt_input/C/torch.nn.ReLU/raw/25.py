import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply ReLU activation
relu = nn.ReLU(inplace=False)
output_tensor = relu(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after ReLU:")
print(output_tensor)