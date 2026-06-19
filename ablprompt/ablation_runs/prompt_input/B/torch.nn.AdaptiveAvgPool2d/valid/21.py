import torch
from torch.nn import AdaptiveAvgPool2d

# Create an instance of AdaptiveAvgPool2d with output size (3, 4)
pool = AdaptiveAvgPool2d((3, 4))

# Create a random input tensor with shape (1, 3, 8, 16)
input_tensor = torch.randn(1, 3, 8, 16)

# Apply the adaptive average pooling
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 3, 3, 4])