import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 28, 28)

# Define a Dropout layer with dropout probability of 0.5
dropout_layer = nn.Dropout(p=0.5)

# Apply the Dropout layer to the input tensor
output_tensor = dropout_layer(input_tensor)

print(output_tensor)