import torch
normalized_shape = [3]
eps = 1e-05
elementwise_affine = False
bias = False
layer_norm = torch.nn.LayerNorm(normalized_shape, eps=eps, elementwise_affine=elementwise_affine, bias=bias)