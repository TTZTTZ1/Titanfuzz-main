import torch

# Task 2: Generate input data
input_tensor = torch.randn(10, 20)
normalized_shape = [20]

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape=normalized_shape)
output_tensor = layer_norm(input_tensor)