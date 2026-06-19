import torch

# Create a random tensor
input_tensor = torch.randn(10, 5)

# Define dropout rate
dropout_rate = 0.2

# Create a Dropout layer
dropout_layer = torch.nn.Dropout(dropout_rate)

# Apply dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)