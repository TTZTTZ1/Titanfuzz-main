import torch
from torch.nn import GELU

# Create an instance of the GELU activation function
gelu = GELU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the GELU activation function to the input tensor
output_tensor = gelu(input_tensor)

print(output_tensor)