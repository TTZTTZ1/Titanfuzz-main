import torch

# Prepare input data
normalized_shape = [3]
eps = 1e-05
elementwise_affine = True
bias = True

# Create an instance of LayerNorm
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)

# Example input tensor
input_tensor = torch.randn(2, 3)

# Call the API
output_tensor = layer_norm(input_tensor)