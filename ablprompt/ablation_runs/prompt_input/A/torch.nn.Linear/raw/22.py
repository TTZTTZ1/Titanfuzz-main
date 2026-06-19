import torch

# Create an instance of Linear layer with input features=10 and output features=5
linear_layer = torch.nn.Linear(10, 5)

# Generate random input tensor of shape (3, 10)
input_tensor = torch.randn(3, 10)

# Pass the input tensor through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)