import torch

# Create an input tensor
input_tensor = torch.randn(1, 4, 8, 8)

# Define the Fold parameters
output_size = (2, 2)
kernel_size = (2, 2)
stride = (2, 2)
padding = (0, 0)

# Apply the Fold operation
folded_tensor = torch.nn.functional.fold(input_tensor, output_size, kernel_size, stride, padding)

print(folded_tensor.shape)  # Output should be [1, 4, 4, 4]