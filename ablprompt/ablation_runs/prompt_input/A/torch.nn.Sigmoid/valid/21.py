import torch
import torch.nn as nn

# Create a Sigmoid activation function instance
sigmoid = nn.Sigmoid()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the sigmoid function to the input tensor
output_tensor = sigmoid(input_tensor)

print(output_tensor)