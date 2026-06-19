import torch
import torch.nn as nn

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply SiLU activation
silu_layer = nn.SiLU()
output = silu_layer(x)

print("Input:", x)
print("Output:", output)