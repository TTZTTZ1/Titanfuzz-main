import torch
import torch.nn as nn

# Create an instance of Tanh
tanh = nn.Tanh()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Tanh to the input tensor
output_tensor = tanh(input_tensor)

print(output_tensor)