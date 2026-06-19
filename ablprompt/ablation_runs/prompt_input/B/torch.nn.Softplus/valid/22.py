import torch
from torch import nn

# Create a Softplus layer with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=30.0)

# Define an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Apply the Softplus activation function
output_tensor = softplus(input_tensor)

print("Input:", input_tensor)
print("Output:", output_tensor)