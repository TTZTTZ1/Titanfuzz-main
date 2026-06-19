import torch
from torch.nn import Dropout

# Create a dropout layer with a dropout probability of 0.5
dropout_layer = Dropout(p=0.5)

# Example input tensor
input_tensor = torch.randn(3, 4)  # A batch of 3 samples, each with 4 features

# Apply dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)