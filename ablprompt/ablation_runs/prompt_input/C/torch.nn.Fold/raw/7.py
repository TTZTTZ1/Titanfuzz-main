import torch

# Define the input tensor dimensions
input_tensor = torch.randn(1, 16, 8, 8)  # Batch size 1, 16 channels, 8x8 grid

# Define the Fold parameters
kernel_size = 2
output_size = (4, 4)
stride = 2
padding = 0
dilation = 1

# Create the Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)