import torch

# Prepare input data
normalized_shape = [3]
eps = 1e-05
elementwise_affine = True
bias = True

# Create an instance of LayerNorm
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)

# Input tensor to normalize
input_tensor = torch.randn(1, 3)

# Call the API
output = layer_norm(input_tensor)