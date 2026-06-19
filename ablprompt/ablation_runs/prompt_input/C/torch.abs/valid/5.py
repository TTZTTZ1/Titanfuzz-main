import torch

# Create a complex tensor
input_tensor = torch.tensor([-1.5, -2.3, 0.7, 4.2], dtype=torch.float)

# Compute the absolute values
abs_tensor = torch.abs(input_tensor)

print(abs_tensor)