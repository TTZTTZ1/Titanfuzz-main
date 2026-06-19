import torch

# Prepare valid input data
normalized_shape = [3]
eps = 1e-05
elementwise_affine = False
bias = True

# Ensure the constraint is satisfied
if not bias or elementwise_affine:
    # Create a random tensor to apply LayerNorm
    x = torch.randn(2, 3)
    layer_norm = torch.nn.LayerNorm(normalized_shape, eps=eps, elementwise_affine=elementwise_affine, bias=bias)
    output = layer_norm(x)
    print(output)
else:
    raise ValueError("Constraint violated: not bias or elementwise_affine")