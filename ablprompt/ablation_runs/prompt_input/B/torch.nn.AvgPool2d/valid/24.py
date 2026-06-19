import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define AvgPool2d layer with specific parameters
avg_pool = nn.AvgPool2d(kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))

# Apply the AvgPool2d layer to the input tensor
output_tensor = avg_pool(input_tensor)

print(output_tensor.shape)