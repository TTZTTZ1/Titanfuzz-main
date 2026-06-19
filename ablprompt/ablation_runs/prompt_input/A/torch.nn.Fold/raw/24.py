import torch

# Define input tensor and parameters for Fold operation
input_tensor = torch.randn(1, 32, 64, 64)
output_size = (16, 16)
kernel_size = (4, 4)
stride = (2, 2)

# Create a Fold layer
fold_layer = torch.nn.Fold(output_size, kernel_size, stride)

# Apply Fold to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)