import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Define a sample input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the LeakyReLU activation function
output_tensor = leaky_relu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)