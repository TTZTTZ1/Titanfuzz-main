import torch

# Create a complex tensor
input_tensor = torch.tensor([[-1+2j], [3-4j], [-5+6j]], dtype=torch.complex64)

# Compute the absolute values
abs_tensor = torch.abs(input_tensor)

print(abs_tensor)