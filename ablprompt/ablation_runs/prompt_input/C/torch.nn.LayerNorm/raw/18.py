import torch
import torch.nn as nn

# Example usage of LayerNorm for an image-like tensor [batch_size, channels, height, width]
input_tensor = torch.randn(32, 3, 224, 224)
layer_norm = nn.LayerNorm(normalized_shape=[3, 224, 224], eps=1e-6, elementwise_affine=True)

normalized_tensor = layer_norm(input_tensor)
print(normalized_tensor.shape)  # Should print: torch.Size([32, 3, 224, 224])