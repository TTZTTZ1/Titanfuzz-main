import torch
input_data = torch.randn(3, 4)
normalized_shape = 4
eps = 1e-05
elementwise_affine = False
bias = False
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
output = layer_norm(input_data)