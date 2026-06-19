import torch
from torch import nn
import numpy as np

# Create a random input tensor
input_tensor = torch.tensor(np.random.randn(3, 4), dtype=torch.float32)

# Define the Sigmoid layer
sigmoid_layer = nn.Sigmoid()

# Apply the Sigmoid layer to the input tensor
output_tensor = sigmoid_layer(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after Sigmoid:")
print(output_tensor)