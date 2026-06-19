import torch
import torch.nn as nn

# Create a Linear layer with 10 input features and 5 output features
linear_layer = nn.Linear(in_features=10, out_features=5)

# Generate random input tensor with shape (batch_size, in_features)
batch_size = 32
input_tensor = torch.randn(batch_size, 10)

# Apply the linear transformation
output_tensor = linear_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: (32, 5)