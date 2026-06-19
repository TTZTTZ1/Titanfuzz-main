import torch

# Create an input tensor
input_tensor = torch.randn(1, 1, 4, 4)

# Define the kernel size and stride for Unfold
kernel_size = (2, 2)
stride = (1, 1)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size=kernel_size, stride=stride)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor)