import torch

# Create a tensor to fold
input_tensor = torch.randn(1, 32, 8, 8)

# Define the Fold parameters
output_size = (4, 4)
kernel_size = (2, 2)
stride = (2, 2)
padding = (0, 0)
dilation = (1, 1)

# Apply the Fold operation
folded_tensor = torch.nn.functional.fold(input_tensor, output_size, kernel_size, stride, padding, dilation)

print(folded_tensor.shape)  # Output should be [1, 32, 4, 4]