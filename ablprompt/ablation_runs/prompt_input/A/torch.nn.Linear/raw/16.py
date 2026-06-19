import torch

# Define the input size, output size, and bias flag for Linear layer
in_features = 10
out_features = 5
bias = True

# Create an instance of torch.nn.Linear
linear_layer = torch.nn.Linear(in_features, out_features, bias)

# Generate random input tensor
input_tensor = torch.randn(in_features)

# Pass the input through the linear layer
output_tensor = linear_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)