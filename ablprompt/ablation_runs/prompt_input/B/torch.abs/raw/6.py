import torch

# Create a complex tensor
input_tensor = torch.tensor([-3+4j, -1-1j, 0+2j], dtype=torch.complex64)

# Compute the absolute values
abs_values = torch.abs(input_tensor)

print(abs_values)