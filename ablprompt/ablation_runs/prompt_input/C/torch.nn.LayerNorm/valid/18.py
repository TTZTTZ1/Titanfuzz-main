import torch
import torch.nn as nn

# Example usage of LayerNorm for image data
input_tensor = torch.randn(32, 3, 224, 224)  # Batch size 32, 3 channels, 224x224 images
layer_norm = nn.LayerNorm((3, 224, 224))
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be the same shape as input_tensor