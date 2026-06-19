import torch

# Define the input tensor dimensions
input_tensor = torch.randn(1, 64, 8, 8)

# Define the Fold parameters
output_size = (16, 16)
kernel_size = (4, 4)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Create the Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: [1, 64, 16, 16]