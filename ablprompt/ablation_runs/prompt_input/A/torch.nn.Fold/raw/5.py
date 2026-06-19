import torch

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 8, 8)
output_size = (4, 4)
kernel_size = (2, 2)
stride = (2, 2)

# Create an instance of Fold
fold = torch.nn.Fold(output_size, kernel_size, stride)

# Apply Fold to the input tensor
output_tensor = fold(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 32, 4, 4])