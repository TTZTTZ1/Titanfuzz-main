import torch
import torch.nn as nn

# Create a ReLU activation function
relu = nn.ReLU(inplace=True)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Apply ReLU activation
output_tensor = relu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)