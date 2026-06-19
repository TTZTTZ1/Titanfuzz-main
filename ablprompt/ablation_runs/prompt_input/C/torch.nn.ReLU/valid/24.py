import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 5)

# Apply ReLU activation
relu = nn.ReLU(inplace=False)
output_tensor = relu(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor after ReLU:\n", output_tensor)