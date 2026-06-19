import torch
from torch.nn import SiLU

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
siLU = SiLU()
output_tensor = siLU(input_tensor)

print(output_tensor)