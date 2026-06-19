import torch
from torch.nn import Dropout

# Create a random tensor
input_tensor = torch.randn(10, 20)

# Initialize Dropout layer with dropout probability of 0.5
dropout_layer = Dropout(p=0.5)

# Apply Dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print(output_tensor)