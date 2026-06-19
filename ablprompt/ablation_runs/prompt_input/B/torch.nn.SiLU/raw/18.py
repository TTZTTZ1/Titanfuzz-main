import torch
from torch import nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
siLU = nn.SiLU()
output_tensor = siLU(input_tensor)

print(output_tensor)