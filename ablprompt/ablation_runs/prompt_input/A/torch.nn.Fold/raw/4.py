import torch

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 64, 64)
output_size = (8, 8)
kernel_size = 4
stride = 2
padding = 0

# Create an instance of Fold
fold = torch.nn.Fold(output_size, kernel_size, stride, padding)

# Apply Fold to the input tensor
output_tensor = fold(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 32, 8, 8])