import torch

# Example usage of LayerNorm for image data normalization
batch_size, channels, height, width = 32, 3, 224, 224
input_tensor = torch.randn(batch_size, channels, height, width)

# Define LayerNorm for the last three dimensions (channels, height, width)
layer_norm = torch.nn.LayerNorm(normalized_shape=[channels, height, width])

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should be [32, 3, 224, 224]