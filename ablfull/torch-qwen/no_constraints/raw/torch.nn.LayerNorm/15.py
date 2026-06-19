import torch

# Task 2: Generate input data
normalized_shape = [3]
input_data = torch.randn(4, 3)
eps = 1e-05
elementwise_affine = True
bias = True

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
output = layer_norm(input_data)