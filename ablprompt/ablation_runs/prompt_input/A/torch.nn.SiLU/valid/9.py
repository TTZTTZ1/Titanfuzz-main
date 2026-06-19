import torch
import torch.nn as nn

# Create an instance of the SiLU activation function
silu = nn.SiLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the SiLU activation function to the input tensor
output_tensor = silu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)