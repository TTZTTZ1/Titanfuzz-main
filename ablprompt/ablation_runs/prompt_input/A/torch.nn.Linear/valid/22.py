import torch

# Create an instance of torch.nn.Linear
linear_layer = torch.nn.Linear(in_features=10, out_features=5)

# Generate some random input data
input_data = torch.randn(32, 10)  # Batch size of 32, 10 features each

# Pass the input data through the linear layer
output_data = linear_layer(input_data)

print(output_data)