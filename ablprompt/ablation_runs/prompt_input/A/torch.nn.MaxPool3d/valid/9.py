import torch
from torch.nn import MaxPool3d

# Create a random tensor of shape (1, 1, 2, 4, 4)
input_tensor = torch.randn(1, 1, 2, 4, 4)

# Define the MaxPool3d layer with kernel size (2, 2, 2) and stride (2, 2, 2)
max_pool_layer = MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool_layer(input_tensor)

print(output_tensor)