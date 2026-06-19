import torch
import torch.nn as nn

# Define a simple linear layer
linear_layer = nn.Linear(in_features=10, out_features=5)

# Create some random input data
input_data = torch.randn(3, 10)  # Batch size of 3, 10 features each

# Pass the input data through the linear layer
output_data = linear_layer(input_data)

print(output_data)