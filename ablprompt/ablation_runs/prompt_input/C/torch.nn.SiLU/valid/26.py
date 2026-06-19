import torch

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0])

# Apply SiLU activation
silu_layer = torch.nn.SiLU()
output = silu_layer(x)

print(output)