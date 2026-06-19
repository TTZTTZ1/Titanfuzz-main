import torch
input_tensor = torch.randn(3, 4)
normalized_shape = [4]
eps = 1e-05
elementwise_affine = False
bias = True
if ((not bias) or elementwise_affine):
    layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)