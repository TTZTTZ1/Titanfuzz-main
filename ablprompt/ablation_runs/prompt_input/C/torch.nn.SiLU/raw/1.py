import torch
from torch import nn

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply SiLU activation
silu = nn.SiLU()
output = silu(x)

# Compute the gradient
output.sum().backward()

print("Input:", x)
print("Output:", output)
print("Gradient:", x.grad)