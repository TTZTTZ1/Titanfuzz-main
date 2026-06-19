import torch
import torch.nn as nn

# Create an instance of Sigmoid
sigmoid = nn.Sigmoid()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Sigmoid function
output_tensor = sigmoid(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Sigmoid:", output_tensor)