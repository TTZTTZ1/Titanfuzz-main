import torch
from torch.nn import AdaptiveAvgPool2d

# Create an input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define the adaptive average pooling layer
pool = AdaptiveAvgPool2d((7, 7))

# Apply the pooling layer to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)