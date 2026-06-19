import torch
from torch import nn

# Create a dropout layer with a dropout probability of 0.5
dropout_layer = nn.Dropout(p=0.5)

# Example input tensor
input_tensor = torch.randn(3, 4)  # Batch size of 3, feature size of 4

# Apply dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)