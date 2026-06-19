import torch
import torch.nn as nn

# Create a dropout layer with a dropout probability of 0.5
dropout_layer = nn.Dropout(p=0.5)

# Example input tensor
input_tensor = torch.randn(3, 4)  # A batch of 3 samples, each with 4 features

# Apply dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nOutput Tensor after Dropout:")
print(output_tensor)