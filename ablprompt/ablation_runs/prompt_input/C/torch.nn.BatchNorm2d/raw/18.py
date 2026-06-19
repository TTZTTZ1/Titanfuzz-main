import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(32, 3, 224, 224)

# Initialize BatchNorm2d layer with 3 feature channels
batch_norm = nn.BatchNorm2d(num_features=3)

# Apply batch normalization to the input tensor
output_tensor = batch_norm(input_tensor)

print(output_tensor.shape)  # Output should be (32, 3, 224, 224)