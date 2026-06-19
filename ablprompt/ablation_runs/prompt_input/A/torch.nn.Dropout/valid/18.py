import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(3, 5)

# Define a Dropout layer with dropout probability of 0.2
dropout_layer = nn.Dropout(p=0.2)

# Apply the Dropout layer to the input tensor
output_tensor = dropout_layer(input_tensor)

print(output_tensor)