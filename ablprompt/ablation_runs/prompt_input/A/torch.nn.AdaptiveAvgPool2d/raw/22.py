import torch
from torch.nn import AdaptiveAvgPool2d

# Example input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Create an instance of AdaptiveAvgPool2d
pool = AdaptiveAvgPool2d((1, 1))

# Apply the adaptive average pooling
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 1, 1])