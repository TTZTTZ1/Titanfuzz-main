import torch

# Prepare input data
normalized_shape = [3]
eps = 1e-05
elementwise_affine = True
bias = True

# Create a random tensor as input to LayerNorm
input_tensor = torch.randn(2, 3)

# Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
output = layer_norm(input_tensor)