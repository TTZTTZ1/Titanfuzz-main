import torch
import torch.nn as nn

# Create a Dropout layer with a dropout probability of 0.5
dropout_layer = nn.Dropout(p=0.5)

# Example input tensor
input_tensor = torch.randn(1, 3, 28, 28)  # Batch size 1, 3 channels, 28x28 image

# Apply the Dropout layer to the input tensor
output_tensor = dropout_layer(input_tensor)

print(output_tensor)