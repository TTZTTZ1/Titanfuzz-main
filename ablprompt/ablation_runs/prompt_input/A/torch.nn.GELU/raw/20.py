import torch
import torch.nn as nn

# Create an instance of GELU activation function
gelu = nn.GELU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply GELU to the input tensor
output_tensor = gelu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after GELU:", output_tensor)