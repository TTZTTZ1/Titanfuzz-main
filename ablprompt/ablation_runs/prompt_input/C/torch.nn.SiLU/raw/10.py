import torch
import torch.nn as nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
siLU_layer = nn.SiLU()
output_tensor = siLU_layer(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after SiLU Activation:")
print(output_tensor)