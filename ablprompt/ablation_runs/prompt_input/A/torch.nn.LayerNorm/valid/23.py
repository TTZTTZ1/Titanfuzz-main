import torch

# Create an input tensor
input_tensor = torch.randn(10, 20)

# Define LayerNorm parameters
normalized_shape = (20,)
eps = 1e-5
elementwise_affine = True

# Initialize LayerNorm layer
layer_norm = torch.nn.LayerNorm(normalized_shape, eps=eps, elementwise_affine=elementwise_affine)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)