import torch
import torch.nn as nn

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply GELU activation function
gelu_layer = nn.GELU()
output_tensor = gelu_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after GELU:", output_tensor)