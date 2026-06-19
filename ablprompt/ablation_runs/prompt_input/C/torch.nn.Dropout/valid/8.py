import torch
from torch.nn import Dropout

# Create a dropout layer with a dropout probability of 0.2
dropout_layer = Dropout(p=0.2)

# Example input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)