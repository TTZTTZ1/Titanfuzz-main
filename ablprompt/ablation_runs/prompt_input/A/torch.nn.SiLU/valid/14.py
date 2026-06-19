import torch
from torch.nn import SiLU

# Create an instance of SiLU (Swish activation function)
swish = SiLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the Swish activation function to the input tensor
output_tensor = swish(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)