import torch
import torch.nn as nn

# Create an instance of ReLU
relu = nn.ReLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply ReLU to the input tensor
output_tensor = relu(input_tensor)

print(output_tensor)