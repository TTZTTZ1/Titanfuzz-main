import torch

# Task 2: Generate input data
input_data = torch.randn(10, 20)
normalized_shape = 20
eps = 1e-05
elementwise_affine = True
bias = True

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
output = layer_norm(input_data)