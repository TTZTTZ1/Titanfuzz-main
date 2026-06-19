import torch

# Task 2: Generate input data
normalized_shape = [3]
input_tensor = torch.randn(4, 3)

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape)
output_tensor = layer_norm(input_tensor)