import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Initialize Dropout layer with dropout probability of 0.2
dropout_layer = torch.nn.Dropout(p=0.2)

# Apply Dropout to the input tensor
output_tensor = dropout_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Dropout:", output_tensor)