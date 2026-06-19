import torch
import torch.nn as nn

# Create an instance of ReLU activation function
relu = nn.ReLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply ReLU activation
output_tensor = relu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ReLU:", output_tensor)