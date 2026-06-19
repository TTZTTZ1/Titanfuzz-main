import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5, 5)

# Define the MaxPool3d layer with various parameters
max_pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(1, 1, 1), padding=(1, 1, 1), dilation=(1, 1, 1), return_indices=True, ceil_mode=False)

# Apply the MaxPool3d layer to the input tensor
output_tensor, indices = max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)
print("Indices Shape:", indices.shape)