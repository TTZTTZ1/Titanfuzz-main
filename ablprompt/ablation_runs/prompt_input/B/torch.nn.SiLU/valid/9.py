import torch
from torch.nn import SiLU

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply SiLU activation
silu = SiLU()
y = silu(x)

# Compute gradients
y.sum().backward()

print("Input:", x)
print("Output:", y)
print("Gradients:", x.grad)