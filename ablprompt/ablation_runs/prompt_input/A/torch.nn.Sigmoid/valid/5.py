import torch
import torch.nn as nn

# Create an instance of the Sigmoid function
sigmoid = nn.Sigmoid()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the sigmoid function to the input tensor
output_tensor = sigmoid(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)