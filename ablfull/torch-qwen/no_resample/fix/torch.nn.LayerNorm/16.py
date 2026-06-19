import torch
normalized_shape = [3]
eps = 1e-05
elementwise_affine = False
bias = True
if ((not bias) or elementwise_affine):
    x = torch.randn(2, 3)
    layer_norm = torch.nn.LayerNorm(normalized_shape, eps=eps, elementwise_affine=elementwise_affine, bias=bias)
    output = layer_norm(x)
    print(output)