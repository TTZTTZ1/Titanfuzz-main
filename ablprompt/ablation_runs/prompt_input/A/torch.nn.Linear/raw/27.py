import torch

# Define input and output dimensions for the Linear layer
in_features = 10
out_features = 5

# Create an instance of torch.nn.Linear
linear_layer = torch.nn.Linear(in_features, out_features)

# Generate random input tensor
input_tensor = torch.randn(3, in_features)  # Batch size of 3

# Forward pass through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)