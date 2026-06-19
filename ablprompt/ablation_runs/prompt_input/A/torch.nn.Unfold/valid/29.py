import torch

# Define input tensor and parameters for Unfold
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size 1, 3 channels, 4x4 spatial dimensions
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size=kernel_size, stride=stride, padding=padding)

# Apply Unfold to the input tensor
output = unfold(input_tensor)

print(output.shape)  # Output shape should be [1, 12, 9] for this example