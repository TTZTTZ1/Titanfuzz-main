import torch
from torch.nn import AdaptiveMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the adaptive max pooling layer
pool = AdaptiveMaxPool2d((16, 16))

# Apply the adaptive max pooling to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 16, 16])