import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(32, 3, 224, 224)

# Initialize BatchNorm2d layer with 3 feature maps
bn_layer = nn.BatchNorm2d(num_features=3)

# Apply batch normalization to the input tensor
output_tensor = bn_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([32, 3, 224, 224])