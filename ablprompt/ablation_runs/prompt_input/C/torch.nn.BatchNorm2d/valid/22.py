import torch
import torch.nn as nn

# Create a dummy input tensor
input_tensor = torch.randn(32, 3, 224, 224)

# Initialize BatchNorm2d layer
batch_norm = nn.BatchNorm2d(num_features=3)

# Apply batch normalization
output_tensor = batch_norm(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([32, 3, 224, 224])