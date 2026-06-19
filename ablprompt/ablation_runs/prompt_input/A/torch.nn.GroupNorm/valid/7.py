import torch
import torch.nn as nn

# Create an input tensor of shape (10, 3, 28, 28)
input_tensor = torch.randn(10, 3, 28, 28)

# Initialize GroupNorm with num_groups=3 and num_channels=3
group_norm = nn.GroupNorm(num_groups=3, num_channels=3)

# Apply GroupNorm to the input tensor
output_tensor = group_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 3, 28, 28])