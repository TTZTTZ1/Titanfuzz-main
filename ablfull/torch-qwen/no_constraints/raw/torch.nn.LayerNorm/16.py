import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4)
normalized_shape = [4]
eps = 1e-05
elementwise_affine = True
bias = True

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
output = layer_norm(input_tensor)