import torch
from torch.nn import AdaptiveAvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define the adaptive average pooling layer
pool = AdaptiveAvgPool2d((14, 14))

# Apply the adaptive average pooling to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 14, 14])