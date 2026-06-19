import torch
import torch.nn as nn

# Create a random input tensor with shape (1, 1, 4, 4, 4)
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Define the MaxPool3d layer with specific parameters
max_pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=0, dilation=1, return_indices=False, ceil_mode=False)

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)