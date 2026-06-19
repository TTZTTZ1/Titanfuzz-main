import torch

# Create a random input tensor
input_tensor = torch.randn(3, 256)

# Define LayerNorm parameters
normalized_shape = (256,)
eps = 1e-05
elementwise_affine = True

# Initialize LayerNorm layer
layer_norm = torch.nn.LayerNorm(normalized_shape, eps=eps, elementwise_affine=elementwise_affine)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)