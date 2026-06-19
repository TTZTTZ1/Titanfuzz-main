import torch
import torch.nn as nn

# Create an instance of Softplus with custom beta and threshold
softplus = nn.Softplus(beta=0.5, threshold=15.0)

# Define a random input tensor
input_tensor = torch.randn(3, 4)

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)