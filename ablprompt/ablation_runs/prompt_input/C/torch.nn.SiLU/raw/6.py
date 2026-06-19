import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
siLU = torch.nn.SiLU()
output_tensor = siLU(input_tensor)

print(output_tensor)