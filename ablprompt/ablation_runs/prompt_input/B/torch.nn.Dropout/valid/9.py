import torch
from torch.nn import Dropout

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Initialize Dropout layer with probability 0.2
dropout_layer = Dropout(p=0.2)

# Apply Dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)