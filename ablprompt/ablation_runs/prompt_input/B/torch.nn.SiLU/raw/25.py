import torch
from torch.nn import SiLU

# Create a random tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply SiLU activation
silu_layer = SiLU()
output_tensor = silu_layer(input_tensor)

print(output_tensor)