import torch
input_tensor = torch.randn(3, 4)
normalized_shape = [4]
eps = 1e-05
elementwise_affine = True
bias = True
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
output_tensor = layer_norm(input_tensor)