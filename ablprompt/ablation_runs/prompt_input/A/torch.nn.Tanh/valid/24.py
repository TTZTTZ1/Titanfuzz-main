import torch
import torch.nn as nn

# Create a Tanh activation function instance
tanh = nn.Tanh()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Apply the Tanh function to the input tensor
output_tensor = tanh(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Tanh:", output_tensor)