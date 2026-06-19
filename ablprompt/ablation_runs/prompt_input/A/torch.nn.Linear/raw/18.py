import torch

# Create a linear layer with 10 input features and 5 output features
linear_layer = torch.nn.Linear(10, 5)

# Generate random input data of shape (3, 10)
input_data = torch.randn(3, 10)

# Pass the input data through the linear layer
output_data = linear_layer(input_data)

print(output_data)