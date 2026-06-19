import torch
import torch.nn as nn

# Create an input tensor of shape (N, C_in, D_out * H_out * W_out)
input_tensor = torch.randn(1, 3, 2, 4)

# Define the Fold layer parameters
output_size = (2, 2)
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)

# Create a Fold layer
fold_layer = nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)