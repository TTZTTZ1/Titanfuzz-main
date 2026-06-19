import torch

# Create a complex tensor
input_tensor = torch.tensor([-1.5 + 2j, -3.0 - 4j, 5.5 + 6.0j])

# Compute the absolute values
abs_tensor = torch.abs(input_tensor)

print(abs_tensor)