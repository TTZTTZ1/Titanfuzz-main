import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 4)
pool = nn.AdaptiveAvgPool2d((3, 4))

# Example input tensor with shape (1, 6, 8)
input_tensor = torch.randn(1, 6, 8)

# Apply the pooling layer
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 6, 3, 4])