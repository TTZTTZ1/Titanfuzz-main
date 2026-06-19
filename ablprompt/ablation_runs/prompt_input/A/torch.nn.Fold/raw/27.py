import torch

# Create an input tensor
input_tensor = torch.randn(1, 4, 8, 8)

# Define Fold parameters
output_size = (2, 2)
kernel_size = (2, 2)
stride = (2, 2)
padding = (0, 0)

# Create a Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: [1, 4*2*2, 2, 2]