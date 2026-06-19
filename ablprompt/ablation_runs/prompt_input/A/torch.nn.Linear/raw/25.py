import torch

# Define a simple linear model using torch.nn.Linear
linear_model = torch.nn.Linear(in_features=10, out_features=5)

# Example input tensor
input_tensor = torch.randn(3, 10)  # Batch size of 3, features of 10

# Forward pass through the linear model
output_tensor = linear_model(input_tensor)

print(output_tensor)