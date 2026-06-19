import torch
import torch.nn as nn

# Create an example input tensor
input_tensor = torch.randn(10, 3, 28, 28)  # Batch size of 10, 3 channels, 28x28 spatial dimensions

# Define GroupNorm layer
group_norm = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)