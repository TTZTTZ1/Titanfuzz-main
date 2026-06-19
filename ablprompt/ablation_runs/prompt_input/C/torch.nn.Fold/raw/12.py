import torch

# Example input tensor
input_tensor = torch.randn(1, 96, 8)

# Define Fold parameters
output_size = (6, 6)
kernel_size = (3, 3)
dilation = 1
padding = 1
stride = 1

# Create Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, dilation=dilation, padding=padding, stride=stride)

# Apply Fold layer to input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)