import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
output_tensor = torch.nn.SiLU()(input_tensor)

print(output_tensor)