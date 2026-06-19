import torch
import torch.nn as nn

# Create a Tanh layer
tanh_layer = nn.Tanh()

# Example input tensor
input_tensor = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0], dtype=torch.float32)

# Apply the Tanh activation
output_tensor = tanh_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)