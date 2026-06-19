import torch
import torch.nn as nn

# Create a Linear layer with 10 input features and 5 output features
linear_layer = nn.Linear(in_features=10, out_features=5)

# Generate random input data with shape (3, 10)
input_data = torch.randn(3, 10)

# Apply the linear transformation
output_data = linear_layer(input_data)

print(output_data.shape)  # Should print: torch.Size([3, 5])