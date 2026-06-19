import torch

# Define input dimensions
input_tensor = torch.randn(1, 16, 8)

# Define Fold parameters
output_size = (4, 4)
kernel_size = (2, 2)
stride = (2, 2)
padding = (0, 0)
dilation = (1, 1)

# Create Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)