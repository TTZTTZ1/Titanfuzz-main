import torch
from torch.nn import SiLU

# Create an instance of SiLU
silu = SiLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply SiLU activation function
output_tensor = silu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying SiLU:", output_tensor)