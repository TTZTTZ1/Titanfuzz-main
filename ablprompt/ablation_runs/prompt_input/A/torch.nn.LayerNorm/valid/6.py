import torch

# Create a random input tensor
input_tensor = torch.randn(10, 20)

# Define the LayerNorm layer with normalized_shape=20 and eps=1e-5
layer_norm = torch.nn.LayerNorm(normalized_shape=20, eps=1e-5)

# Apply LayerNorm to the input tensor
normalized_tensor = layer_norm(input_tensor)

print("Original Tensor:", input_tensor)
print("Normalized Tensor:", normalized_tensor)