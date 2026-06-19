import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus_layer = nn.Softplus(beta=0.5, threshold=10.0)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Apply the Softplus activation function
output_tensor = softplus_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)