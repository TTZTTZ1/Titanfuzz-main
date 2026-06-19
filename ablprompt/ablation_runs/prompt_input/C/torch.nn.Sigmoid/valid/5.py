import torch
import torch.nn as nn

# Create a Sigmoid layer
sigmoid_layer = nn.Sigmoid()

# Example input tensor
input_tensor = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])

# Apply the Sigmoid function
output_tensor = sigmoid_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)