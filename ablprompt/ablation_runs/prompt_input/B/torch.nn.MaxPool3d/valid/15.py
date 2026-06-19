import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 7, 9)

# Define the MaxPool3d layer
max_pool = nn.MaxPool3d(kernel_size=(2, 3, 4), stride=(1, 2, 3), padding=(1, 1, 1), dilation=(1, 1, 1))

# Apply the max pooling operation
output_tensor = max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)