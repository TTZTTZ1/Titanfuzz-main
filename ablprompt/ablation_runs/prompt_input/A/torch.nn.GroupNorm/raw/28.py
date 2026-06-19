import torch
import torch.nn as nn

# Create a sample input tensor
input_tensor = torch.randn(10, 3, 224, 224)

# Define the GroupNorm layer
group_norm = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply the GroupNorm layer to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)