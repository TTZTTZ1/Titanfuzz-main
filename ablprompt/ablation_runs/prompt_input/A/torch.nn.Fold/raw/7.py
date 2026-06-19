import torch

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 64, 64)
output_size = (16, 16)
kernel_size = (4, 4)
stride = (2, 2)
padding = (0, 0)

# Create an instance of Fold
fold = torch.nn.Fold(output_size, kernel_size, stride, padding)

# Apply Fold to the input tensor
output_tensor = fold(input_tensor)

print(output_tensor.shape)  # Output should be [1, 32, 16, 16]