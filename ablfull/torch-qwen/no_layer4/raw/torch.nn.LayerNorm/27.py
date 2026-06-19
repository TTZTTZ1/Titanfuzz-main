import torch

# Prepare valid input data
normalized_shape = [3]
eps = 1e-05
elementwise_affine = False
bias = True

# Ensure the constraint is satisfied
if not bias or elementwise_affine:
    layer_norm = torch.nn.LayerNorm(normalized_shape, eps, elementwise_affine, bias)
else:
    raise ValueError("Constraint violated: not bias or elementwise_affine")

# Call the API
output = layer_norm(torch.randn(2, 3))