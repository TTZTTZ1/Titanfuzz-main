import torch

# Define input tensor and parameters for Fold operation
input_tensor = torch.randn(1, 32, 8, 8)
output_size = (4, 4)
kernel_size = (2, 2)
stride = (2, 2)

# Create a Fold layer
fold_layer = torch.nn.Fold(output_size, kernel_size, stride)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 32, 4, 4])