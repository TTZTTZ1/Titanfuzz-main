import torch
import torch.nn as nn

# Create a random 5D tensor of shape (1, 1, 2, 4, 6)
input_tensor = torch.randn(1, 1, 2, 4, 6)

# Define a MaxPool3d layer with kernel size (2, 2, 2) and stride (1, 1, 1)
maxpool_layer = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(1, 1, 1))

# Apply the MaxPool3d layer to the input tensor
output_tensor = maxpool_layer(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 1, 2, 4, 6])