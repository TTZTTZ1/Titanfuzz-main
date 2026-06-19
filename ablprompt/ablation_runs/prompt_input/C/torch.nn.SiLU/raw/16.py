import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
silu_layer = nn.SiLU()
output_tensor = silu_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after SiLU:", output_tensor)