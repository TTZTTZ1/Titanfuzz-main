import torch

# Create an input tensor
input_tensor = torch.randn(10, 3)

# Define LayerNorm
layer_norm = torch.nn.LayerNorm(normalized_shape=(3,), eps=1e-5, elementwise_affine=True)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor)