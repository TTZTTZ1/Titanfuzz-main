import torch
import torch.nn as nn

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply GELU activation function
gelu_function = nn.GELU()
output_tensor = gelu_function(input_tensor)

print(output_tensor)