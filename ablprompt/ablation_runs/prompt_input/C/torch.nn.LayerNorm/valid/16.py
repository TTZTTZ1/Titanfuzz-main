import torch

# Define the normalized shape for the LayerNorm
normalized_shape = [3, 4]

# Create a LayerNorm layer
layer_norm = torch.nn.LayerNorm(normalized_shape)

# Create a random input tensor with shape (2, 3, 4)
input_tensor = torch.randn(2, *normalized_shape)

# Apply LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print("Input Tensor:", input_tensor)
print("LayerNorm Output:", output_tensor)