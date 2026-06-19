import torch

# Create an instance of Linear layer with 10 input features and 5 output features
linear_layer = torch.nn.Linear(in_features=10, out_features=5)

# Example input tensor with shape (2, 10)
input_tensor = torch.randn(2, 10)

# Forward pass through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)