import torch
import torch.nn as nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply Sigmoid activation
sigmoid = nn.Sigmoid()
output_tensor = sigmoid(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)