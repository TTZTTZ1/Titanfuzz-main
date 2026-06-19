import torch
import torch.nn as nn

# Create a random input tensor with shape (1, 3, 4, 5, 6)
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define MaxPool3d layer with specific parameters
max_pool_layer = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=(0, 0, 0))

# Apply the max pooling operation
output_tensor = max_pool_layer(input_tensor)

print(output_tensor.shape)  # Output should be (1, 3, 2, 2, 3)