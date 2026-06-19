import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation using torch.nn.SiLU
silu_layer = nn.SiLU()
output_tensor = silu_layer(input_tensor)

print(output_tensor)