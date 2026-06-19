import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 224, 224)
input_tensor = torch.randn(1, 3, 224, 224)

# Initialize BatchNorm2d layer with 3 channels
batch_norm_layer = nn.BatchNorm2d(num_features=3)

# Apply batch normalization to the input tensor
output_tensor = batch_norm_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 224, 224])