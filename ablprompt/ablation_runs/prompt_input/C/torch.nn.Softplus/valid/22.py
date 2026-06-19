import torch
import torch.nn as nn

# Create an instance of Softplus with custom beta and threshold
softplus = nn.Softplus(beta=0.5, threshold=10.0)

# Generate random input tensor
input_tensor = torch.randn(3, 3)

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after Softplus Activation:")
print(output_tensor)