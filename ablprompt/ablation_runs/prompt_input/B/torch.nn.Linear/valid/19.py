import torch
import torch.nn as nn

# Create a Linear layer with 5 input features and 10 output features
linear_layer = nn.Linear(in_features=5, out_features=10)

# Generate random input tensor with shape (3, 5)
input_tensor = torch.randn(3, 5)

# Apply the linear transformation
output_tensor = linear_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: (3, 10)