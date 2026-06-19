import torch
import torch.nn as nn

# Create an instance of the Tanh activation function
tanh = nn.Tanh()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the Tanh function to the input tensor
output_tensor = tanh(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying Tanh:", output_tensor)