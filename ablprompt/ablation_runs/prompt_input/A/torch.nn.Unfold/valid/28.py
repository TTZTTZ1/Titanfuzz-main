import torch

# Define input tensor and parameters for Unfold
input_tensor = torch.randn(1, 3, 28, 28)  # Batch size=1, Channels=3, Height=28, Width=28
kernel_size = (3, 3)
stride = (1, 1)
padding = (0, 0)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size, stride, padding)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output shape will be [1, 9, 26, 26]