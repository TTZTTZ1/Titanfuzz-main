import torch
import torch.nn as nn

# Create an instance of LeakyReLU
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply LeakyReLU to the input tensor
output_tensor = leaky_relu(input_tensor)

print(output_tensor)