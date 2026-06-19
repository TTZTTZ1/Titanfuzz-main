import torch
import torch.nn as nn

# Create a random 5D tensor with shape (1, 1, 2, 4, 4)
input_tensor = torch.randn(1, 1, 2, 4, 4)

# Define the MaxPool3d layer with kernel size of 2 and stride of 2
maxpool_layer = nn.MaxPool3d(kernel_size=2, stride=2)

# Apply the MaxPool3d layer to the input tensor
output_tensor = maxpool_layer(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 1, 1, 2, 2])