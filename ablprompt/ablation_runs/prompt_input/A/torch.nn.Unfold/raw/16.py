import torch
from torch.nn import Unfold

# Create a tensor to unfold
input_tensor = torch.randn(1, 3, 4, 4)

# Define the kernel size and stride for unfolding
kernel_size = (2, 2)
stride = (1, 1)

# Initialize the Unfold layer
unfold_layer = Unfold(kernel_size=kernel_size, stride=stride)

# Apply the Unfold layer to the input tensor
output_tensor = unfold_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be (1, 12, 3, 3)