import torch

# Prepare input data
normalized_shape = 3
eps = 1e-06
elementwise_affine = False
bias = True

# Check constraint
assert not bias or elementwise_affine, "Constraint violation"

# Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape=normalized_shape, eps=eps, elementwise_affine=elementwise_affine, bias=bias)