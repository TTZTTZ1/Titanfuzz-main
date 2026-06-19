import torch
import torch.nn as nn

# Create a dropout layer with a dropout probability of 0.3
dropout_layer = nn.Dropout(p=0.3)

# Example tensor
input_tensor = torch.randn(4, 4)

# Apply dropout
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)