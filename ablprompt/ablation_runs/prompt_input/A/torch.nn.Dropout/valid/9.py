import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(3, 5)

# Define the dropout rate
dropout_rate = 0.5

# Create a Dropout layer
dropout_layer = nn.Dropout(dropout_rate)

# Apply the Dropout layer to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)