import torch

# Create a random input tensor
input_tensor = torch.randn(32, 128, requires_grad=True)

# Define the LayerNorm layer with specific parameters
layer_norm = torch.nn.LayerNorm(normalized_shape=(128,), eps=1e-6, elementwise_affine=False, bias=False)

# Apply the LayerNorm to the input tensor
output_tensor = layer_norm(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([32, 128])