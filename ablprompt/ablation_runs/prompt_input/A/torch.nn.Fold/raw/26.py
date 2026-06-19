import torch

# Define input tensor and parameters for Fold operation
input_tensor = torch.randn(1, 32, 64, 64)  # Batch size, channels, height, width
output_size = (32, 32)  # Output spatial dimensions
kernel_size = (8, 8)  # Kernel spatial dimensions
stride = (4, 4)  # Stride for sliding window
padding = (0, 0)  # Padding added to both sides of the input

# Create a Fold layer
fold_layer = torch.nn.Fold(output_size, kernel_size, stride, padding)

# Apply Fold operation
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)