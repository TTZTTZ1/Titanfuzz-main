import torch

# Prepare valid input data
normalized_shape = [3]
eps = 1e-05
elementwise_affine = False
bias = True

# Ensure the constraint is satisfied
if not bias or elementwise_affine:
    layer_norm = torch.nn.LayerNorm(normalized_shape, eps=eps, elementwise_affine=elementwise_affine, bias=bias)
else:
    raise ValueError("Constraint violation: bias must be False if elementwise_affine is False")

# Call the API
input_tensor = torch.randn(2, 3)
output_tensor = layer_norm(input_tensor)