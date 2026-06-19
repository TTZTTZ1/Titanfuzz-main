import torch
from torch.nn import SiLU

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
silu = SiLU()
output_tensor = silu(input_tensor)

print(output_tensor)