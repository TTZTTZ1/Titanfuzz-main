
import torch
normalized_shape = [3]
eps = 1e-05
elementwise_affine = False
bias = False
device = 'cpu'
dtype = None
layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias, device, dtype)
