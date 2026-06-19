import torch
from torch.nn import SiLU

# Create a random tensor
x = torch.randn(3, 4)

# Apply SiLU activation
silu = SiLU()
output = silu(x)

print(output)